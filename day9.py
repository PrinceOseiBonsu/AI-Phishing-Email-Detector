# Day 9 - Exploring Your Dataset
# Phishing Email Detector Project

import pandas as pd
#-----Load dataset----
df = pd.read_csv("Enron.csv")

# --- Add body length BEFORE splitting ---
df["body_length"] = df["body"].str.len()

#---- Split into phishing nd legitimate ---
phishing = df[df["label"] == 1]
legitimate = df[df['label'] == 0]

print("="* 50)
print("DATASET EXPLORATION")
print("="* 50)
print("=" * 50)

print(f"\nTotal emails: {len(df)}")
print(f"Phishing emails: {len(phishing)}")
print(f"Legitimate emails: {len(legitimate)}")

# --- Look at real examples ---
print("\n--- 3 Real Phishing Emails ---")
print(phishing["subject"].head(3).to_string())

print("\n--- 3 Real Legitimate Emails ---")
print(legitimate["subject"].head(3).to_string())

# --- Email length analysis ---
df["body_length"] = df["body"].str.len()

print("\n--- Email Length Analysis ---")
print(f"Average phishing email length: {phishing['body_length'].mean():.0f} characters")
print(f"Average legitimate email length: {legitimate['body_length'].mean():.0f} characters")


print("\n--- Most Common Words in Phishing Subjects ---")
phishing_subjects = " ".join(phishing["subject"].dropna())
words = phishing_subjects.lower().split()
word_count  = {}
for word in words:
    if len(word) > 3:
        word_count[word] = word_count.get(word, 0) + 1



# --- Most common words in phishing emails ---
top_words = sorted(word_count.items(), key=lambda x: x[1], reverse = True)[:10]
for word, count in top_words:
    print(f"  '{word}' appears {count} times")

# --- Most common words in legitimate emails ---


print("\n--- Most Common Words in Legitimate Subjects ---")
legitimate_subjects = " ".join(legitimate["subject"].dropna())
words = legitimate_subjects.lower().split()
word_count = {}
for word in words:
    if len(word) > 3:
        word_count[word] = word_count.get(word, 0) + 1
top_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)[:10]
for word, count in top_words:
    print(f" '{word}' appears {count} times")



