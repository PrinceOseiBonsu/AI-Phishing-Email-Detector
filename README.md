# 🛡️ AI Phishing Email Detector

> Machine learning powered phishing detection system trained on 29,767 real emails achieving **98.44% accuracy**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Accuracy](https://img.shields.io/badge/Accuracy-98.44%25-green)
![ML](https://img.shields.io/badge/ML-Random%20Forest-orange)

---

## 📌 Overview

Phishing attacks cost businesses billions every year. Traditional keyword-based detectors fail because attackers constantly evolve their language to avoid detection.

This project combines **machine learning** and **manual security features** to detect phishing emails with 98.44% accuracy — catching 99.2% of all phishing emails.

---

## 🚀 Key Results

| Metric | Score |
|--------|-------|
| Accuracy | 98.44% |
| Phishing Recall | 99.2% |
| ROC-AUC | 0.9981 |
| False Negatives | 22 out of 2,769 |
| Training Data | 23,813 emails |
| Test Data | 5,954 emails |

---

## 🧠 How It Works

Raw Email → Clean Text → Extract Features → Predict → Explain

### Two types of features:

**1. TF-IDF Features (10,000)**
Automatically scores word importance across 29,767 emails.
Words like "click", "verify", "suspended" score high in phishing emails.

**2. Manual Security Features (5)**
- Body length
- Subject length
- Link count
- Has links (binary)
- Urgency score

**Combined: 10,005 features per email**

### Model: Random Forest Classifier
- 100 decision trees voting on each prediction
- Majority vote = final prediction
- Significantly outperforms Naive Bayes (81% → 98.44%)

---

## 📊 Data Analysis Findings

From analyzing 29,767 real emails:

- Phishing emails have **3.7x more links** than legitimate
- Phishing subjects are **23% longer** on average
- Phishing bodies are **18% shorter** than legitimate
- **31%** of phishing emails contain links vs only **7%** of legitimate

---

## 🗂️ Project Structure
AI-Phishing-Email-Detector/
│
├── day21.py          ← Command line detector (main)
├── day19.py          ← Model training pipeline
├── day17.py          ← Classifier development
├── day13.py          ← Feature engineering
├── week2project.py   ← Full data analysis report
│
└── charts/
├── confusion_matrix.png
├── chart1_distribution.png
├── chart2_body_length.png
├── chart3_phishing_words.png
└── chart4_links.png

---

## 🛠️ Tech Stack

- **Python** — core language
- **scikit-learn** — Random Forest, TF-IDF, model evaluation
- **pandas** — data manipulation
- **numpy** — numerical computing
- **matplotlib** — data visualization
- **pickle** — model persistence
- **scipy** — sparse matrix operations

---

## 📈 Model Performance

![Confusion Matrix](confusion_matrix.png)

---

## 🔮 Coming Soon

- [ ] OpenAI API integration for threat explanation
- [ ] Flask web interface
- [ ] Gmail API integration
- [ ] Microsoft Outlook API integration
- [ ] Live deployment with public URL

---

## 👨🏾‍💻 Author

**Prince Osei Bonsu**
Computer Science & Cybersecurity — Voorhees University
GPA: 4.0/4.0

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/prince-osei-bonsu)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/PrinceOseiBonsu)

---

*Built as part of a deliberate learning journey toward a career in security engineering*
