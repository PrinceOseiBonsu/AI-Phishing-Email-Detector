# Day 17 - Building Your First Classifier
# Phishing Email Detector Project

import pandas as pd
import numpy as np
import re
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")
df["body"] = df["body"].fillna("")
df["subject"] = df["subject"].fillna("")

# --- Clean text for model ---
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

print("=" * 50)
print("BUILDING FIRST CLASSIFIER")
print("=" * 50)

# --- Prepare data ---
X_text = df["text"]
y = df["label"]
manual_features = ["body_length", "subject_length",
                   "link_count", "has_links", "urgency_score"]
X_manual = df[manual_features].values

print(f"\nTotal emails: {len(df)}")
print(f"Phishing: {y.sum()}")
print(f"Legitimate: {(y == 0).sum()}")

# --- Train/test split ---
X_train_text, X_test_text, y_train, y_test, X_train_manual, X_test_manual = train_test_split(
    X_text, y, X_manual, test_size=0.2, random_state=42
)

print(f"\nTraining set: {len(X_train_text)} emails")
print(f"Test set: {len(X_test_text)} emails")

# --- TF-IDF vectorization ---
vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english",
    min_df=2,
    ngram_range=(1, 2),
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train_text)
X_test_tfidf = vectorizer.transform(X_test_text)

# --- Combine TF-IDF + manual features ---
X_train_combined = sp.hstack([X_train_tfidf, X_train_manual])
X_test_combined = sp.hstack([X_test_tfidf, X_test_manual])

print(f"\nCombined training shape: {X_train_combined.shape}")

# --- Train model ---
print("\nTraining model...")
model = RandomForestClassifier(n_estimators=100, random_state = 42)
model.fit(X_train_combined, y_train)
print("Model trained!")

# --- Predictions ---
y_pred = model.predict(X_test_combined)

# --- Results ---
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred,
      target_names=["Legitimate", "Phishing"]))