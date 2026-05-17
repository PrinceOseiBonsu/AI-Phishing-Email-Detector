import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")
df["body"] = df["body"].fillna("")

print("=" * 50)
print("TF-IDF VECTORIZATION")
print("=" * 50)

# --- Step 1: Create TF-IDF vectorizer ---
vectorizer = TfidfVectorizer(
    max_features=5000,      # keep only top 5000 words
    stop_words="english",   # remove english stopwords automatically
    min_df=2                # word must appear in at least 2 emails
)


# --- Step 2: Fit and transform ---
X = vectorizer.fit_transform(df["body"])
y = df["label"]


print(f'\nSample features (words): {df.shape}')
print(f'TF-IDF matrix shape: {X.shape}')
print(f'This means: {X.shape[0]} emails * {X.shape[1]} wordd features')

# --- Step 3: Look at top words ---
feature_names = vectorizer.get_feature_names_out()
print((f'\nSample features (wwords): {feature_names[:10].tolist()}'))


# --- Step 4: Inspect one email ---
print('\n--- Inspecting first phishing email---')
phishing_idx = df[df['label']==1].index[0]
email_vector = X[phishing_idx]

# Get top scoring words for this email
import numpy as np

scores = email_vector.toarray()[0]
top_indices = np.argsort(scores)[::-1][:10]

print("Top 10 most important words:")
for idx in top_indices:
    if scores[idx] > 0:
        print(f"  '{feature_names[idx]}': {scores[idx]:.4f}")
