#Day 10 - Cleaning Messy Data
#Phishing Email Detector Project

import pandas as pd


# #-----Load datatest -----
# df = pd.read_csv("Enron.csv")

# print("="*50)
# print("BEFORE CLEANING")
# print("="*50)
# print(f"Missing Subjects:{df['subject'].isnull().sum()}")
# print(f"Sample body text:")
# print(df['body'][0][:200])


# # --- Fix 1: Fill missing subjects ---
# df['subject'] = df['subject'].fillna("No Subject")

# # --- Fix 2: Clean body text ---
# def clean_text(text):
#     if pd.isnull(text):
#         return ""
#     text = str(text)
#     text = text.replace("\r\n", " ")
#     text = text.replace("\n"," ")
#     text = text.replace("\r", " ")
#     text = " ".join(text.split())
#     text = text.lower()
#     return text
# df['subject'] = df['subject'].apply(clean_text)
# df['body'] = df['body'].apply(clean_text)

# print("\n" + "=" * 50)
# print("AFTER CLEANING")
# print("=" * 50)
# print(f"Missing subjects: {df['subject'].isnull().sum()}")
# print(f"Sample body text:")
# print(df['body'][0][:200])

# # --- Save clean dataset ---
# df.to_csv("Enron_clean.csv", index= False)
# print("\nClean dataset saved to Enron_clean.csv")
# print(f"Total emails cleaned: {len(df)}")



# df = pd.read_csv("Enron_clean.csv")

# df['clean_data'] = df['subject'].fillna("").str.len()

# phishing = df[df['label']==1]
# legitimate = df[df['label']==0]

# average_phishing = phishing['clean_data'].mean()
# average_legitimate  = legitimate['clean_data'].mean()

# count = 0
# for word in phishing['subject']:
#     if len(word) > 50:
#         count += 1
# print(f"There are {count} words in the phishing email")

# print("Average_phishing:", average_phishing)
# print("Average_legitimate:", average_legitimate)



# print("\n---- 3 Phishing Emails---")
# print(phishing['subject'].head(3))

# print("\n---- 3 Legitimate Emails---")
# print(legitimate['subject'].head(3))




df = pd.read_csv("Enron.csv")
df['subject_length'] = df['subject'].fillna("").str.len()
phishing = df[df['label']==1]
legitimate = df[df['label']==0]

average_phishing = phishing['subject_length'].mean()
average_legitimate = legitimate['subject_length'].mean()

print("Average Phishing", average_phishing)
print("Average Legitimate", average_legitimate)

print("\n---Three Phishing Emails---")
print(phishing['subject'].head(3))

print("\n---Three Legitimate Emails---")
print(legitimate['subject'].head(3))