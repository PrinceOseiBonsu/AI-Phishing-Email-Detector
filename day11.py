# Day 11 - Finding Patterns in Phishing Emails
# Phishing Email Detector Project

import pandas as pd

# --- Load clean dataset ---
df = pd.read_csv("Enron_clean.csv")

df["body_length"] = df["body"].str.len()
df["subject_length"] = df["subject"].str.len()

phishing = df[df["label"] == 1]
legitimate = df[df["label"] == 0]

print("=" * 50)
print("PATTERN ANALYSIS")
print("=" * 50)

# --- Pattern 1: Email length ---
print("\n--- Email Body Length ---")
print(f"Average phishing body:   {phishing['body_length'].mean():.0f} chars")
print(f"Average legitimate body: {legitimate['body_length'].mean():.0f} chars")

print("\n--- Email Subject Length ---")
print(f"Average phishing subject:   {phishing['subject_length'].mean():.0f} chars")
print(f"Average legitimate subject: {legitimate['subject_length'].mean():.0f} chars")

# --- Pattern 2: Top words ---
def get_top_words(emails, column, n=10):
    text = " ".join(emails[column].fillna(""))
    words = text.lower().split()
    stopwords = ["the", "and", "for", "you", "are", "this",
                 "that", "with", "have", "from", "will", "your",
                 "our", "not", "all", "can", "was", "but", "they"]
    word_count = {}
    for word in words:
        clean = word.strip(".,!?:;\"'()")
        if len(clean) > 3 and clean not in stopwords:
            word_count[clean] = word_count.get(clean, 0) + 1
    top = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:n]
    return top

print("\n--- Top 10 Words in Phishing Bodies ---")
for word, count in get_top_words(phishing, "body"):
    print(f"  '{word}': {count}")

print("\n--- Top 10 Words in Legitimate Bodies ---")
for word, count in get_top_words(legitimate, "body"):
    print(f"  '{word}': {count}")

# --- Pattern 3: Link count ---
def count_links(text):
    if pd.isnull(text):
        return 0
    words = str(text).split()
    return sum(1 for word in words if word.startswith("http"))

df["link_count"] = df["body"].apply(count_links)
phishing = df[df["label"] == 1]
legitimate = df[df["label"] == 0]

print("\n--- Link Count Analysis ---")
print(f"Average links in phishing:   {phishing['link_count'].mean():.2f}")
print(f"Average links in legitimate: {legitimate['link_count'].mean():.2f}")
print(f"Phishing emails with links:  {(phishing['link_count'] > 0).sum()}")
print(f"Legitimate emails with links:{(legitimate['link_count'] > 0).sum()}")

# --- Pattern 4: Most common domains in phishing links ---
# --- Pattern 4: Most common domains in phishing links ---

def get_domain(link):
    parts = link.split('/')
    if len(parts) > 2:
        return parts[2]
    return None

domain_count = {}

for text in phishing['body']:
    if pd.isnull(text):
        continue

    words = text.split()

    for i, word in enumerate(words):
        if word == "http":
            if i + 2 < len(words):
                domain = words[i + 2]   # likely domain part
                
                # rebuild domain like example.com
                if i + 3 < len(words):
                    domain = domain + "." + words[i + 3]

                domain_count[domain] = domain_count.get(domain, 0) + 1

top_domains = sorted(domain_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("\n--- Most Common Domains in Phishing Links ---")
for domain, count in top_domains:
    print(f"'{domain}': {count}")