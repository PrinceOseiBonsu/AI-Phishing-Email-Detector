# retrain.py
# Retrain model with combined modern + Enron dataset

import pandas as pd
import numpy as np
import scipy.sparse as sp
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("Loading datasets...")

# --- Load Enron dataset ---
enron = pd.read_csv("data/Enron_clean.csv")
enron = enron[["subject", "body", "label"]]
enron["subject"] = enron["subject"].fillna("")
enron["body"] = enron["body"].fillna("")
print(f"Enron dataset: {len(enron)} emails")

# --- Load modern phishing dataset ---
modern = pd.read_csv("Phishing_Email.csv")
print("Modern dataset columns:", modern.columns.tolist())
print(modern.head(3))


# --- Clean modern dataset ---
modern = modern[["Email Text", "Email Type"]]
modern.columns = ["body", "label"]
modern["subject"] = ""
modern["label"] = modern["label"].map({
    "Safe Email": 0,
    "Phishing Email": 1
})
modern["body"] = modern["body"].fillna("")
print(f"Modern dataset: {len(modern)} emails")
print(f"Modern phishing: {modern['label'].sum()}")
print(f"Modern legitimate: {(modern['label'] == 0).sum()}")

# --- Combine datasets ---
combined = pd.concat([enron, modern], ignore_index=True)
combined = combined.dropna(subset=["label"])
print(f"\nCombined dataset: {len(combined)} emails")
print(f"Total phishing: {combined['label'].sum()}")
print(f"Total legitimate: {(combined['label'] == 0).sum()}")

# --- Clean text ---
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

combined["text"] = combined["subject"].apply(clean_text) + " " + combined["body"].apply(clean_text)

# --- Manual features ---
def count_links(text):
    return str(text).split().count("http")

def urgency_score(text):
    urgency_words = ["urgent", "immediately", "now",
                     "suspended", "verify", "click",
                     "limited", "warning", "important"]
    text_lower = str(text).lower()
    return sum(1 for word in urgency_words if word in text_lower)

combined["body_length"] = combined["body"].str.len()
combined["subject_length"] = combined["subject"].str.len()
combined["link_count"] = combined["body"].apply(count_links)
combined["has_links"] = (combined["link_count"] > 0).astype(int)
combined["urgency_score"] = combined["body"].apply(urgency_score)

# --- Prepare data ---
X_text = combined["text"]
y = combined["label"].astype(int)
manual_features = ["body_length", "subject_length",
                   "link_count", "has_links", "urgency_score"]
X_manual = combined[manual_features].values

# --- Train/test split ---
X_train_text, X_test_text, y_train, y_test, X_train_manual, X_test_manual = train_test_split(
    X_text, y, X_manual, test_size=0.2, random_state=42
)

print(f"\nTraining set: {len(X_train_text)} emails")
print(f"Test set: {len(X_test_text)} emails")

# --- TF-IDF ---
print("\nVectorizing...")
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
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_combined, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test_combined)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred,
      target_names=["Legitimate", "Phishing"]))

# --- Save new model ---
print("Saving new model...")
with open("models/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("New model saved successfully!")
print("Restart your Flask app to use the new model.")