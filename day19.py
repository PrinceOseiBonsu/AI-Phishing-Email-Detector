# Day 19 - Saving and Loading Your Model
# Phishing Email Detector Project

import pandas as pd
import numpy as np
import re
import scipy.sparse as sp
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")
df["body"] = df["body"].fillna("")
df["subject"] = df["subject"].fillna("")

# --- Clean text ---
def clean_for_model(text):
    if pd.isnull(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["text"] = df["subject"].apply(clean_for_model) + " " + df["body"].apply(clean_for_model)

# --- Manual features ---
df["body_length"] = df["body"].str.len()
df["subject_length"] = df["subject"].str.len()
df["link_count"] = df["body"].apply(lambda x: str(x).split().count("http"))
df["has_links"] = (df["link_count"] > 0).astype(int)
df["urgency_score"] = df["body"].apply(lambda x: sum(
    1 for word in ["urgent", "verify", "click", "suspended", "immediately"]
    if word in str(x).lower()
))

# --- Prepare data ---
X_text = df["text"]
y = df["label"]
manual_features = ["body_length", "subject_length",
                   "link_count", "has_links", "urgency_score"]
X_manual = df[manual_features].values

# --- Train/test split ---
X_train_text, X_test_text, y_train, y_test, X_train_manual, X_test_manual = train_test_split(
    X_text, y, X_manual, test_size=0.2, random_state=42
)

# --- TF-IDF ---
vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english",
    min_df=2,
    ngram_range=(1, 2),
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train_text)
X_test_tfidf = vectorizer.transform(X_test_text)

# --- Combine features ---
X_train_combined = sp.hstack([X_train_tfidf, X_train_manual])
X_test_combined = sp.hstack([X_test_tfidf, X_test_manual])

# --- Train model ---
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_combined, y_train)

# --- Check accuracy ---
y_pred = model.predict(X_test_combined)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# --- Save model and vectorizer ---
print("\nSaving model...")
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model saved to phishing_model.pkl")
print("Vectorizer saved to vectorizer.pkl")

# --- Test loading ---
print("\nTesting model loading...")
with open("phishing_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    loaded_vectorizer = pickle.load(f)

print("Model loaded successfully!")

# --- Test on a real email ---
print("\n--- Testing on new emails ---")

def predict_email(subject, body, model, vectorizer):
    clean = clean_for_model(subject + " " + body)
    tfidf = vectorizer.transform([clean])
    
    body_length = len(body)
    subject_length = len(subject)
    link_count = body.split().count("http")
    has_links = 1 if link_count > 0 else 0
    urgency_score = sum(1 for word in 
        ["urgent", "verify", "click", "suspended", "immediately"]
        if word in body.lower())
    
    manual = np.array([[body_length, subject_length,
                        link_count, has_links, urgency_score]])
    combined = sp.hstack([tfidf, manual])
    
    prediction = model.predict(combined)[0]
    probability = model.predict_proba(combined)[0]
    
    return {
        "prediction": "Phishing" if prediction == 1 else "Legitimate",
        "confidence": f"{max(probability) * 100:.1f}%"
    }

# Test 1 - obvious phishing
result1 = predict_email(
    "URGENT: Your account suspended",
    "Click here immediately to verify your account or it will be deleted http://paypa1.com",
    loaded_model, loaded_vectorizer
)
print(f"\nTest 1 (phishing): {result1}")

# Test 2 - legitimate
result2 = predict_email(
    "Team meeting tomorrow",
    "Hi everyone just a reminder about our team meeting tomorrow at 3pm in the conference room",
    loaded_model, loaded_vectorizer
)
print(f"Test 2 (legitimate): {result2}")

# Test 3 - your own test
result3 = predict_email(
    "You have won a prize",
    "Congratulations you have been selected to receive a cash prize click here now to claim",
    loaded_model, loaded_vectorizer
)
print(f"Test 3 (phishing): {result3}")