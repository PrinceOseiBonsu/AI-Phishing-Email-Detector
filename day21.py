# Day 21 - Week 3 Mini Project
# Command Line Phishing Detector

import pickle
import numpy as np
import scipy.sparse as sp
import re


# --- Load saved model and vectorizer ---
with open("phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# --- Clean text function ---
def clean_for_model(text):
    if text == "":
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', " ", text)
    text = re.sub(r'\s+', " ", text)
    return text.strip()


# --- Extract manual features function ---
def extract_manual_features(subject,body):
    body_length = len(body)
    subject_length = len(subject)
    link_count = body.lower().count("http")
    has_links = int(link_count > 0) 
    urgency_words = ["urgent", "verify", "click", "suspended", "immediately"]
    urgency_score = sum( 1 for word in urgency_words if word in body.lower())
    return [ body_length, subject_length, link_count, has_links, urgency_score]
# --- Predict function ---
# takes subject and body
# returns prediction, confidence, risk level, keywords found
# your code here
def predict_email(subject,body):
    text = clean_for_model(body) + " " + clean_for_model(subject)
    text_tfidf = vectorizer.transform([text])
    manual_X = extract_manual_features(subject, body)
    manual_X = np.array(manual_X).reshape(1, -1)
    combined_X = sp.hstack([text_tfidf, manual_X])
    prediction = model.predict(combined_X)
    confidence = model.predict_proba(combined_X)
    phishing_confidence = confidence[0][1]
    if phishing_confidence > 0.8:
        risk_level = "High"
    elif phishing_confidence > 0.5:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    urgency_words = ["urgent", "verify", "click", "suspended", "immediately"]
    keywords_found = [ word for word in urgency_words if word in body.lower()]
    return prediction[0], phishing_confidence, risk_level, keywords_found

# --- Main program ---
# ask user to input subject and body
# run prediction
# print full report
# your code here

def main():
    print("=" * 50)
    print("PHISHING EMAIL DETECTOR")
    print("=" * 50)

    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    prediction, confidence, risk_level, keywords = predict_email(subject, body)

    keyword_text = ", ".join(keywords) if keywords else "None"

    print("\n" + "=" * 50)
    print("ANALYSIS RESULT")
    print("=" * 50)

    if prediction == 1:
        print("Prediction:   PHISHING ⚠️")
    else:
        print("Prediction:   LEGITIMATE ✅")

    print(f"Confidence:   {confidence * 100:.1f}%")
    print(f"Risk Level:   {risk_level.upper()}")
    print(f"Keywords:     {keyword_text}")

    print("\n" + "=" * 50)
    print("RECOMMENDATION")
    print("=" * 50)

    if prediction == 1:
        print("→ Do NOT click any links in this email")
        print("→ Do NOT provide any personal information")
        print("→ Report this email to your IT department")
    else:
        print("→ This email appears safer, but still review carefully")
        print("→ Do not click links unless you trust the sender")

    print("=" * 50)


main()