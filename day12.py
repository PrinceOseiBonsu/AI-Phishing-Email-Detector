# Day 12 - Visualizing Your Findings
# Phishing Email Detector Project

import pandas as pd
import matplotlib.pyplot as plt

# --- Load clean dataset ---
df = pd.read_csv("data/Enron_clean.csv")

df["body_length"] = df["body"].str.len()
df["subject_length"] = df["subject"].str.len()

phishing = df[df["label"] == 1]
legitimate = df[df["label"] == 0]

# --- Chart 1: Phishing vs Legitimate count ---
plt.figure(figsize=(10, 6))
plt.bar(["Legitimate", "Phishing"],
        [len(legitimate), len(phishing)],
        color=["green", "red"])
plt.title("Phishing vs Legitimate Emails")
plt.ylabel("Number of Emails")
plt.savefig("chart1_distribution.png")
plt.close()
print("Chart 1 saved")

# --- Chart 2: Average email body length ---
plt.figure(figsize=(10, 6))
plt.bar(["Legitimate", "Phishing"],
        [legitimate["body_length"].mean(), phishing["body_length"].mean()],
        color=["green", "red"])
plt.title("Average Email Body Length")
plt.ylabel("Characters")
plt.savefig("chart2_body_length.png")
plt.close()
print("Chart 2 saved")

# --- Chart 3: Top phishing words ---
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

phishing_words = get_top_words(phishing, "body")
words = [w[0] for w in phishing_words]
counts = [w[1] for w in phishing_words]

plt.figure(figsize=(12, 6))
plt.barh(words, counts, color="red")
plt.title("Top 10 Words in Phishing Emails")
plt.xlabel("Frequency")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("chart3_phishing_words.png")
plt.close()
print("Chart 3 saved")

# --- Chart 4: Link count comparison ---
def count_links(text):
    if pd.isnull(text):
        return 0
    return str(text).split().count("http")

df["link_count"] = df["body"].apply(count_links)
phishing = df[df["label"] == 1]
legitimate = df[df["label"] == 0]

plt.figure(figsize=(10, 6))
plt.bar(["Legitimate", "Phishing"],
        [legitimate["link_count"].mean(), phishing["link_count"].mean()],
        color=["green", "red"])
plt.title("Average Number of Links per Email")
plt.ylabel("Average Links")
plt.savefig("chart4_links.png")
plt.close()
print("Chart 4 saved")

print("\nAll charts saved to your Project1 folder!")
print("Open them to see your findings visualized.")