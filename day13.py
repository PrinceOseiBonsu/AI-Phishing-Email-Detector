# Day 13 - Understanding Features
# Phishing Email Detector Project

import pandas as pd

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")

print("=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50)

# --- Feature 1: Body length ---
df["body_length"] = df["body"].str.len()

# --- Feature 2: Subject length ---
df["subject_length"] = df["subject"].str.len()

# --- Feature 3: Link count ---
def count_links(text):
    if pd.isnull(text):
        return 0
    return str(text).split().count("http")

df["link_count"] = df["body"].apply(count_links)

# --- Feature 4: Has links (binary) ---
df["has_links"] = (df["link_count"] > 0).astype(int)

# --- Feature 5: Urgency score ---
def urgency_score(text):
    if pd.isnull(text):
        return 0
    urgency_words = ["urgent", "immediately", "now",
                     "suspended", "verify", "click",
                     "limited", "warning", "important"]
    text_lower = str(text).lower()
    return sum(1 for word in urgency_words if word in text_lower)

df["urgency_score"] = df["body"].apply(urgency_score)

# --- Feature 6: Subject urgency ---
df["subject_urgency"] = df["subject"].apply(urgency_score)

# --- Feature 7: Count Capital ---
def count_caps_words(text):
    if pd.isnull(text):
        return 0
    return sum(1 for word in text.split() if word== word.upper())

df['count_caps_words'] = df['subject'].apply(count_caps_words)

# --- Show feature matrix ---
print("\nFeature matrix sample (first 5 rows):")
features = ["body_length", "subject_length", "link_count",
            "has_links", "urgency_score", "subject_urgency","count_caps_words","label"]
print(df[features].head(10).to_string())

# --- Feature statistics ---
print("\n--- Feature Averages by Label ---")
print(df.groupby("label")[features[:-1]].mean().to_string())

# --- Save feature matrix ---
df[features].to_csv("features.csv", index=False)
print("\nFeature matrix saved to features.csv")
print(f"Shape: {df[features].shape}")