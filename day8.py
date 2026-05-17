import pandas as pd
import re
from sklearn.model_selection import train_test_split

df = pd.read_csv("Enron_clean.csv")
df['body'] = df['body'].fillna("")
df['subject'] = df['subject'].fillna("")

def clean_for_model(text):
    if pd.isnull(text):
        return "" 
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', " ", text)
    text = re.sub(r'\s+', " ", text)
    return text.strip()
df['text'] = df['body'].apply(clean_for_model)+ " " + df['subject'].apply(clean_for_model)



def manual_features(df):
    df['body_length'] = df['body'].str.len()
    df['subject_length'] = df['subject'].str.len()
    df['link_count'] = df['body'].apply(lambda x: str(x).split().count("http"))
    df['has_links'] = (df['link_count'] > 0).astype(int)
    df['urgency_score'] = df['body'].apply(lambda x: sum(1 for word  in ["urgent", "verify", "click", "suspended", "immediately"] if word in str(x).lower() ))

    return df


df = manual_features(df)

X_text = df['body']
y = df['label']

manual_features = ['body_length', 'subject_length','link_count', 'has_links', 'urgency_score']
X_manual = df[manual_features].values



X_train_text, X_test_text, y_train, y_test, X_train_manual, X_test_manual = train_test_split(
    X_text, y, X_manual, test_size=0.2, random_state=42
)


