# Day 20 - Testing Your Model Properly
# Phishing Email Detector Project

import pandas as pd
import numpy as np
import re
import scipy.sparse as sp
import pickle
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score)

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")
df["body"] = df["body"].fillna("")
df["subject"] = df["subject"].fillna("")

def clean_for_model(text):
    if pd.isnull(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["text"] = df["subject"].apply(clean_for_model) + " " + df["body"].apply(clean_for_model)

df["body_length"] = df["body"].str.len()
df["subject_length"] = df["subject"].str.len()
df["link_count"] = df["body"].apply(lambda x: str(x).split().count("http"))
df["has_links"] = (df["link_count"] > 0).astype(int)
df["urgency_score"] = df["body"].apply(lambda x: sum(
    1 for word in ["urgent", "verify", "click", "suspended", "immediately"]
    if word in str(x).lower()
))

X_text = df["text"]
y = df["label"]
manual_features = ["body_length", "subject_length",
                   "link_count", "has_links", "urgency_score"]
X_manual = df[manual_features].values

X_train_text, X_test_text, y_train, y_test, X_train_manual, X_test_manual = train_test_split(
    X_text, y, X_manual, test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english",
    min_df=2,
    ngram_range=(1, 2),
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train_text)
X_test_tfidf = vectorizer.transform(X_test_text)

X_train_combined = sp.hstack([X_train_tfidf, X_train_manual])
X_test_combined = sp.hstack([X_test_tfidf, X_test_manual])

print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_combined, y_train)

y_pred = model.predict(X_test_combined)
y_prob = model.predict_proba(X_test_combined)[:, 1]

# --- Confusion Matrix ---
print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"\nConfusion Matrix:")
print(f"True Negatives  (correct legitimate): {tn}")
print(f"False Positives (legitimate → phishing): {fp}")
print(f"False Negatives (phishing → legitimate): {fn}")
print(f"True Positives  (correct phishing): {tp}")

print(f"\nMost dangerous mistakes (False Negatives): {fn}")
print(f"That means we missed {fn} real phishing emails")

# --- Key metrics ---
print(f"\nAccuracy:  {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(f"ROC-AUC:   {roc_auc_score(y_test, y_prob):.4f}")

print("\nFull Report:")
print(classification_report(y_test, y_pred,
      target_names=["Legitimate", "Phishing"]))

# --- Save confusion matrix chart ---
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
plt.xticks([0, 1], ['Legitimate', 'Phishing'])
plt.yticks([0, 1], ['Legitimate', 'Phishing'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
for i in range(2):
    for j in range(2):
        plt.text(j, i, str(cm[i, j]),
                ha='center', va='center',
                color='white' if cm[i, j] > cm.max()/2 else 'black')
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()
print("\nConfusion matrix saved to confusion_matrix.png")


