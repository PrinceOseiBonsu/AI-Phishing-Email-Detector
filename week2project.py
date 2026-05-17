
# Week 2 Mini Project — Full Analysis Report
# Phishing Email Detector Project

import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean():
    df = pd.read_csv("Enron.csv")
    df['body'] = df['body'].fillna("")
    df['subject'] = df['subject'].fillna("")

    df.to_csv("Enron_clean.csv", index=False)

    return df

def count_links(text):
    if pd.isnull(text):
        return 0
    words = text.split()
    return sum(1 for word in words if 'http' in word)

def urgency_score(text):
    if pd.isnull(text):
        return 0
    urgency_words= ["urgent", "immediately", "now",
                     "suspended", "verify", "click",
                     "limited", "warning", "important"]
    text_lower = text.lower()
    return sum(1 for word in urgency_words if word in text_lower)

def count_caps_words(text):
    if pd.isnull(text):
        return 0 
    return sum(1 for word in text.split() if word==word.upper())


def build_features(df):
    df['body_length'] = df['body'].str.len()
    df['subject_length'] = df['subject'].str.len()
    df['link_count'] = df['body'].apply(count_links)
    df['urgency_score'] = df['body'].apply(urgency_score)
    df['caps_count'] = df['subject'].apply(count_caps_words)
    df['has_links'] = (df['link_count'] > 0).astype(int)
    df['subject_urgency'] = df['subject'].apply(urgency_score)

    features = ['body_length', 'subject_length', 'link_count',
                'has_links', 'urgency_score',
                'subject_urgency', 'caps_count', 'label']

    df[features].to_csv("features.csv", index=False)

    return df

def print_overview(df):
    total = len(df)
    phishing_count = len(df[df['label']==1])
    legitimate_count = len(df[df['label']==0])
    missing_subject = df['subject'].isnull().sum()
    print('DATASET OVERVIEW')
    print('Total emails:', total)
    print('Phishing:',phishing_count)
    print('Legitimate:', legitimate_count)
    print(f'Missing subjects: {missing_subject} (cleaned)')


def print_feature_analysis(df):
    features = ['body_length', 'subject_length', 'link_count', 'urgency_score', 'caps_count', 'has_links','subject_urgency']
    analysis = df.groupby('label')[features].mean()
    print(analysis)

def save_charts(df):
    phishing = df[df['label']==1]
    legitimate = df[df['label']==0]

    plt.figure(figsize=(10,6))

    plt.bar(['Phishing','Legitimate'],[len(phishing),len(legitimate)],color=['red','green'])
    plt.title('Phishing emails vs Legitimate emails')
    plt.ylabel('number of emails')
    plt.savefig("chart1_distribution.png")
    plt.close()

    plt.figure(figsize=(10,6))
    plt.bar(['Legitimate','Phishing'],[legitimate['body_length'].mean(), phishing['body_length'].mean()],color=('green','red'))
    plt.title('Average Body Length')
    plt.ylabel('Average Body Length')
    plt.savefig('chart2_body_length.png')
    plt.close()
     
    text = " ".join(phishing['body'])
    words = text.split()

    word_count = {}

    for word in words:
        clean = word.strip(',./{]}!&<>').lower()
        word_count[clean] = word_count.get(clean,0) + 1
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse = True)[:10]

    word_labels = [w[0] for w in top_words]
    counts = [w[1] for w in top_words]

    plt.figure(figsize=(10,6))
    plt.barh(word_labels, counts)
    plt.title('Top Phishing Words')
    plt.xlabel('Frequency')
    plt.savefig("chart3_phishing_words.png")
    plt.close()



    plt.figure(figsize=(10,6))
    plt.bar(
    ['Legitimate', 'Phishing'],
    [legitimate['link_count'].mean(), phishing['link_count'].mean()],
    color=['green', 'red'])
    plt.title('Average Link Count Comparison')
    plt.ylabel('Average Number of Links')
    plt.savefig("chart4_links.png")
    plt.close()



def print_key_findings(df):
    phishing = df[df['label'] == 1]
    legitimate = df[df['label'] == 0]

    phishing_body = phishing['body_length'].mean()
    legitimate_body = legitimate['body_length'].mean()

    phishing_subject = phishing['subject_length'].mean()
    legitimate_subject = legitimate['subject_length'].mean()

    phishing_links = phishing['link_count'].mean()
    legitimate_links = legitimate['link_count'].mean()

    phishing_has_links = phishing['has_links'].mean()
    legitimate_has_links = legitimate['has_links'].mean()

    print("\nKEY FINDINGS")

    print(f"→ Phishing emails are {((legitimate_body - phishing_body) / legitimate_body * 100):.0f}% shorter in body")

    print(f"→ Phishing subjects are {((phishing_subject - legitimate_subject) / legitimate_subject * 100):.0f}% longer")

    print(f"→ Phishing emails have {(phishing_links / legitimate_links):.1f}x more links")

    print(f"→ Phishing emails are {(phishing_has_links / legitimate_has_links):.1f}x more likely to contain links")


def print_files_saved():
    print("\nFILES SAVED")
    print("→ Enron_clean.csv")
    print("→ features.csv")
    print("→ chart1_distribution.png")
    print("→ chart2_body_length.png")
    print("→ chart3_phishing_words.png")
    print("→ chart4_links.png")

    print("\n" + "=" * 50)
    print("WEEK 2 COMPLETE — READY FOR ML MODEL")
    print("=" * 50)

def main():
    df = load_and_clean()
    df = build_features(df)
    print_overview(df)
    print_feature_analysis(df)
    save_charts(df)
    print_key_findings(df)
    print_files_saved()

main()