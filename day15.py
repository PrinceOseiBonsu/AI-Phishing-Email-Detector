# Day 15 - NLP Basics
# Phishing Email Detector Project

import pandas as pd

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")

phishing = df[df['label']==1]
legitimate = df[df['label']==0]

# --- Step 1: Tokenization ---
def tokenize(text):
    if pd.isnull(text):
        return []
    text = str(text).lower()
    text = text.strip(".,!?:;\"'()")
    tokens = text.split()
    return tokens

# --- Test tokenization ---
sample_phishing = phishing['body'].iloc[0]
sample_legit = legitimate['body'].iloc[0]

print("=" * 50)
print("TOKENIZATION")
print("=" * 50)

print("\nOriginal phishing email (first 100 chars): ")
print(sample_phishing[:100])

print("\nTokenized:")
print(tokenize(sample_phishing)[:15])

print("\nOriginal legitimate email (first 100 chars):")
print(sample_legit[:100])

print("\nTokenized")
print(tokenize(sample_legit)[:15])

# --- Step 2: Vocabulary building ---
print("\n" + "=" * 50)
print("VOCABULARY")
print("=" * 50)


all_tokens = []
for text in df['body'].head(1000):
    all_tokens.extend(tokenize(text))


vocabulary = list(set(all_tokens))
print(f"Unique words in first 1000 emails: {len(vocabulary)}")
print(f"Sample vocabulary: {vocabulary[:10]}")


# --- Step 3: Why stopwords matter ---
stopwords = ["the", "and", "for", "you", "are", "this",
             "that", "with", "have", "from", "will",
             "your", "our", "not", "all", "can", "was"]


def tokenize_clean(text):
    if pd.isnull(text):
        return []
    tokens = tokenize(text)
    return [t for t in tokens if t not in stopwords and len(t) > 2]



print("\n" + "=" * 50)
print("CLEAN TOKENIZATION")
print("=" * 50)
print("\nBefore removing stopwords:")
print(tokenize(sample_phishing)[:15])
print("\nAfter removing stopwords:")
print(tokenize_clean(sample_phishing)[:15])

all_clean_tokens = []
for text in df['body'].head(1000):
    all_clean_tokens.extend(tokenize_clean(text))

count_words = list(set(all_clean_tokens))
clean_vocabulary = list(set(all_clean_tokens))
print(f"\nVocabulary size before cleaning: {len(vocabulary)}")
print(f"Vocabulary size after cleaning:  {len(clean_vocabulary)}")








