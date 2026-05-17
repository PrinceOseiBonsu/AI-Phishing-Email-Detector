
# Day 1 - Variables and Data Types
# Phishing Email Detector Project

# --- A real phishing email broken into variables ---

# sender = "security@paypa1.com"
# subject = "URGENT: Your account limited"
# body = "Click here immediately to restore your account access or it will be deleted"
# has_attachment = False
# number_of_links = 3
# confidence_score = 0.91
# is_phishing = True

# # --- Now let's inspect what we stored ---

# print("Sender:", sender)
# print("Subject:", subject)
# print("Has attachment:", has_attachment)
# print("Number of links:", number_of_links)
# print("Confidence score:", confidence_score)
# print("Is phishing:", is_phishing)

# # --- Let's ask questions about our data ---

# print("\n--- Analysis ---")
# print("Is URGENT in subject?", "URGENT" in subject)
# print("Subject length:", len(subject), "characters")
# print("Sender domain:", sender.split("@")[1])
# print("Is sender suspicious?", "paypa1" in sender)


# recipient = "your@email.com"
# email_age_days = 2
# reply_to = None

# print("Missing reply-to address:", reply_to is None)


# sender1 = "support@paypal.com"
# sender2 = "support@paypa1.com"
# sender3 = "support@paypal.com.phishing.net"

# # How would you use split("@") and indexing
# # to extract the domain from all three
# # and which ones are suspicious and why?

# print(sender1.split("@")[1])
# print(sender2.split("@")[1])
# print(sender3.split("@")[1])


# Day 2 - Lists and Dictionaries
# Phishing Email Detector Project

# --- A list of suspicious keywords ---
# phishing_keywords = [
#     "urgent",
#     "verify",
#     "suspended",
#     "click here",
#     "limited",
#     "winner"
# ]

# # --- A single email as a dictionary ---
# email = {
#     "sender": "security@paypa1.com",
#     "subject": "URGENT: Your account has been suspended",
#     "body": "Click here immediately to verify your account",
#     "has_attachment": False,
#     "number_of_links": 3,
#     "is_phishing": True
# }

# # --- Access and print email fields ---
# print("Sender:", email["sender"])
# print("Subject:", email["subject"])
# print("Is phishing:", email["is_phishing"])

# # --- Check if any keywords appear in the subject ---
# print("\n--- Keyword Check ---")
# subject_lower = email["subject"].lower()
# for keyword in phishing_keywords:
#     if keyword in subject_lower:
#         print("Suspicious keyword found:", keyword)

# # --- A list of emails ---
# emails = [
#     {
#         "sender": "security@paypa1.com",
#         "subject": "URGENT: Your account suspended",
#         "is_phishing": True
#     },
#     {
#         "sender": "john@gmail.com",
#         "subject": "Hey are we still meeting at 3?",
#         "is_phishing": False
#     },
#     {
#         "sender": "support@bank-secure-login.com",
#         "subject": "Verify your account now",
#         "is_phishing": True
#     }
# ]

# # --- Print how many emails we have ---
# # print("\n--- Email List ---")
# # print("Total emails:", len(emails))
# # print("First email sender:", emails[0]["sender"])
# # print("Last email sender:", emails[2]["sender"])

# print(email[0])

# Write code that:

# Counts how many emails are phishing
# Prints the total number of emails
# Prints how many are phishing
# Prints the phishing rate as a percentage


# emails = [
#     {
#         "sender": "security@paypa1.com",
#         "subject": "URGENT: Your account suspended",
#         "is_phishing": True
#     },
#     {
#         "sender": "john@gmail.com",
#         "subject": "Hey are we still meeting at 3?",
#         "is_phishing": False
#     },
#     {
#         "sender": "support@bank-secure-login.com",
#         "subject": "Verify your account now",
#         "is_phishing": True
#     }
# ]



# print("Total emils:",len(emails))
# count = 0
# for i in emails:
#     if i["is_phishing"]:
#         count +=1
# print("Phishing emails:", count)


# fishing_rate = (count/len(emails))* 100
# print("Phishing rate:", round(fishing_rate, 2))

# Expected output:
# Total emails: 3
# Phishing emails: 2
# Phishing rate: 66.666...%


# Day 3 - Functions
# Phishing Email Detector Project

# --- Function 1: Check if email is phishing ---
# def is_phishing(email):
#     if email["is_phishing"]:
#         return "Phishing"
#     else:
#         return "Legitimate"

# # --- Function 2: Extract domain from sender ---
# def get_domain(sender):
#     return sender.split("@")[1]

# # --- Function 3: Check for suspicious keywords ---
# def check_keywords(subject):
#     phishing_keywords = ["urgent", "verify", "suspended", "click here", "limited", "winner"]
#     subject_lower = subject.lower()
#     found = []
#     for keyword in phishing_keywords:
#         if keyword in subject_lower:
#             found.append(keyword)
#     return found

# # --- Function 4: Count phishing emails ---
# def count_phishing(emails):
#     count = 0
#     for email in emails:
#         if email["is_phishing"]:
#             count += 1
#     return count

# # --- Now let's USE the functions ---
# emails = [
#     {
#         "sender": "security@paypa1.com",
#         "subject": "URGENT: Your account suspended",
#         "is_phishing": True
#     },
#     {
#         "sender": "john@gmail.com",
#         "subject": "Hey are we still meeting at 3?",
#         "is_phishing": False
#     },
#     {
#         "sender": "support@bank-secure-login.com",
#         "subject": "Verify your account now",
#         "is_phishing": True
#     }
# ]

# # --- Test every function ---
# print("--- Testing Functions ---")
# for email in emails:
#     print("\nSender:", email["sender"])
#     print("Domain:", get_domain(email["sender"]))
#     print("Status:", is_phishing(email))
#     print("Keywords found:", check_keywords(email["subject"]))

# print("\n--- Summary ---")
# print("Total emails:", len(emails))
# print("Phishing count:", count_phishing(emails))
# print("Phishing rate:", round(count_phishing(emails) / len(emails) * 100, 2), "%")


# def get_domain(sender):
#     sender.split("@")[1]    # no return

# print(get_domain("security@paypa1.com"))



# You have these functions from earlier in your file. 
# Now I want you to write one new 
# function called analyze_email that:

# Takes a single email dictionary as input
# Uses get_domain(), check_keywords()
#  and is_phishing() that you already built
# Prints a full report for that email like this:

# --- Email Report ---
# Sender: security@paypa1.com
# Domain: paypa1.com
# Status: Phishing
# Keywords found: ['urgent', 'suspended']


# analyze_email({
#     "sender": "security@paypa1.com",
#     "subject": "URGENT: Your account suspended",
#     "is_phishing": True
# })
# Expected output:
# --- Email Report ---
# Sender: security@paypa1.com
# Domain: paypa1.com
# Status: Phishing
# Keywords found: ['urgent', 'suspended']

# def get_domain(sender):
#     return sender.split("@")[1]

# def check_keywords(subject):
#     phishing_keywords = ["urgent", "verify", "suspended", "click here", "limited", "winner"]
#     subject_lower = subject.lower()
#     found = []
#     for keyword in phishing_keywords:
#         if keyword in subject_lower:
#             found.append(keyword)
#     return found

# def is_phishing(email):
#     if email["is_phishing"]:
#         return "Phishing"
#     else:
#         return "Legitimate"

# # STEP 2 - define analyze_email AFTER
# def analyze_email(email):
#     print("\n--- Email Report ---")
#     print("Sender:", email["sender"])
#     print("Domain:", get_domain(email["sender"]))
#     print("Status:", is_phishing(email))
#     print("Keywords:", check_keywords(email["subject"]))

# # STEP 3 - call the function LAST
# analyze_email({
#     "sender": "security@paypa1.com",
#     "subject": "URGENT: Your account suspended",
#     "is_phishing": True
# })

# analyze_email({
#     "sender": "john@gmail.com",
#     "subject": "Hey are we still meeting at 3?",
#     "is_phishing": False
# })

# analyze_email({
#     "sender": "support@bank-secure-login.com",
#     "subject": "Verify your account now",
#     "is_phishing": True
# })




# Day 4 - File Reding and Writting
# Phishing Email Detector Project

# --- PART 1: Reading a file ---

# print("--- Reading emails from file")

# file = open("emails.txt", "r")
# lines = file.readlines()
# file.close()

# print("Total lines read:", len(lines))
# print("First line:", lines[0])

# print("\n--- Processing emails ---")

# emails = []
# for line in lines:
#     line = line.strip()
#     parts = line.split(" | ")
#     email = {
#         "sender": parts[0],
#         "subject": parts[1],
#         "is_phishing": parts[2] == "True"
#     }
#     emails.append(email)

# for email in emails:
#     print(email)

# # --- PART 3: Writting results to a file ---
# print("\n--- Writting results to file ---")

# output = open("results.txt", "w")

# for email in emails:
#     domain = email["sender"].split("@")[1]
#     status = "Phishing" if email["is_phishing"] else "Legitimate"
#     line = f"Sender: {email['sender']} | Domain: {domain} | status: {status}\n"
#     output.write(line)

# output.close()
# print("Results saved to results.txt")



# Day 5 - String Manipulation
# Phishing Email Detector Project

# email_subject = "  URGENT: Click HERE to verify your PayPal account NOW!  "
# email_body = "Dear Customer, your account has been suspended. Click here immediately to restore access. Visit http://paypa1.com/verify now!"
# sender = "security-alert@paypa1-secure.com"

# # --- Basic cleaning ---
# clean_subject = email_subject.strip().lower()
# print("Clean subject:", clean_subject)

# # --- Word extraction ---
# words = clean_subject.split()
# print("Word count:", len(words))
# print("Words:", words)

# # --- Keyword counting ---
# suspicious_words = ["urgent", "click", "verify", "suspended", "immediately"]
# print("\n--- Keyword Analysis ---")
# for word in suspicious_words:
#     count = email_body.lower().count(word)
#     if count > 0:
#         print(f"'{word}' appears {count} time(s)")

# # --- Domain extraction ---
# print("\n--- Domain Analysis ---")
# domain = sender.split("@")[1]
# print("Full domain:", domain)
# real_domain = ".".join(domain.split(".")[-2:])
# print("Real domain:", real_domain)
# print("Is trusted:", real_domain in ["paypal.com", "google.com", "microsoft.com"])

# # --- Link detection ---
# print("\n--- Link Analysis ---")
# words_in_body = email_body.split()
# links = [word for word in words_in_body if word.startswith("http")]
# print("Links found:", links)
# print("Number of links:", len(links))

# # --- Urgency score ---
# print("\n--- Urgency Score ---")
# urgency_words = ["urgent", "immediately", "now", "suspended", "verify"]
# urgency_score = 0
# body_lower = email_body.lower()
# for word in urgency_words:
#     urgency_score += body_lower.count(word)
# print("Urgency score:", urgency_score)




# Day 5 Challenge
# You have everything you need from today. Now write 
# a function called analyze_text that takes an email 
# body as input and returns a dictionary with this information:
# python{
#     "word_count": 10,
#     "link_count": 2,
#     "urgency_score": 4,
#     "keywords_found": ["click", "verify"],
#     "links": ["http://paypa1.com/verify"]
# }
# pythonbody = "Dear Customer, your account has been suspended. Click here immediately to restore access. 
# Visit http://paypa1.com/verify and http://secure-login.net now!"
# Expected output:
# Word count: 18
# Link count: 2
# Urgency score: 5
# Keywords found: ['click', 'suspended', 'immediately', 'verify']
# Links: ['http://paypa1.com/verify', 'http://secure-login.net']
# Rules:
# Must be inside a function called analyze_text
# Must return a dictionary — not just print
# Use everything you learned today — .lower(), .split(), .count(), .startswith()
# No copy pasting — write it yourself

# def analyze_text(body):

#     words = body.split()
#     words_count = len(words)

#     linkcounter = 0
#     new_line = []
#     for word in words:
#         if word.startswith("http://"):
#             linkcounter += 1
#             new_line.append(word)

#     urgency_words = ["urgent", "immediately", "now", "suspended", "verify", "click"]
#     urgency_lst = []

#     urgency_score = 0
#     for word in words:
#         clean_word = word.lower().strip(".,!?:;")
#         if clean_word in urgency_words:
#             urgency_score += 1
#             urgency_lst.append(clean_word)

#     for link in new_line:
#         for word in urgency_words:
#             if word in link:
#                 urgency_score += 1
#                 urgency_lst.append(word)

#     return{"word_count": words_count,
#            "link_count" : linkcounter,
#            "urgency_score" :urgency_score,
#            "keywordss_found": urgency_lst,
#            "links": new_line
#            }

# body = "Dear Customer, your account has been suspended. Click here immediately to restore access. Visit http://paypa1.com/verify and http://secure-login.net now!"

# print(analyze_text(body))
    



# Loop with index AND value together
# Day 6 - Loops and Conditionals
# Phishing Email Detector Project

# emails = [
#     {"sender": "security@paypa1.com", "subject": "URGENT: Account suspended", "urgency_score": 8},
#     {"sender": "john@gmail.com", "subject": "Meeting at 3pm?", "urgency_score": 0},
#     {"sender": "support@bank-secure.com", "subject": "Verify your account", "urgency_score": 5},
#     {"sender": "newsletter@amazon.com", "subject": "Your order has shipped", "urgency_score": 1},
#     {"sender": "alert@paypa1-secure.com", "subject": "Immediately verify now", "urgency_score": 9},
# ]

# # --- Risk classification using if/elif/else ---
# def classify_risk(urgency_score):
#     if urgency_score >= 8:
#         return "Critical"
#     elif urgency_score >= 5:
#         return "High"
#     elif urgency_score >= 2:
#         return "Medium"
#     else:
#         return "Low"
    

# print("\n--- Email Risk Report ---")
# for index, email in enumerate(emails):
#     risk = classify_risk(email["urgency_score"])
#     print(f"\nEmail {index + 1}:")
#     print(f" Sender: {email['sender']}")
#     print(f" Subject: {email['subject']}")
#     print(f" Risk = {risk}")

# print("\n--- Risk Summary---")
# risk_count = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
# for email in emails:
#     risk = classify_risk(email["urgency_score"])
#     risk_count[risk] += 1

# for level, count in risk_count.items():
#     print(f"{level}: {count} email(s)")



# print("\n---Scanning emails---")
# index = 0
# while index < len(emails):
#     email = emails[index]
#     if email["urgency_score"] >= 8:
#         print(f"🚨 Critical threat found: {email['sender']} — stopping scan")
#         break
#     print(f"✓ Email {index + 1} scanned — safe")
#     index += 1



# Expected output:
# Scanning email 1: security@paypa1.com — Critical
# Skipping email 2: empty sender
# Scanning email 3: john@gmail.com — Low
# Scanning email 4: alert@paypa1-secure.com — Critical
# 🚨 2 critical threats found — stopping scan
# Total emails scanned: 4

# def classify_risk(urgency_score):
#     if urgency_score >= 8:
#         return "Critical"
#     elif urgency_score >= 5:
#         return "High"
#     elif urgency_score >= 2:
#         return "Medium"
#     else:
#         return "Low"

# def scan_email(emails):
#     scanned =0
#     critical_count = 0

#     for index, email in enumerate(emails):
#         scanned += 1
#         if email['sender'] == "":
#             print(f"Skippng email {index + 1} empty sender")
#             continue
#         risk = classify_risk(email["urgency_score"])
#         print(f"Scanning email {index + 1} {email['sender']} - {risk}")

#         if risk == "Critical":
#             critical_count += 1
#         if critical_count == 2:
#             print(f"🚨 2 critical threats found — stopping scan")
#             break
#     print("Total emils scanned:", scanned)

            

# emails = [
#     {"sender": "security@paypa1.com", "subject": "URGENT: Account suspended", "urgency_score": 8},
#     {"sender": "", "subject": "Empty sender", "urgency_score": 0},
#     {"sender": "john@gmail.com", "subject": "Meeting at 3pm?", "urgency_score": 0},
#     {"sender": "alert@paypa1-secure.com", "subject": "Immediately verify now", "urgency_score": 9},
#     {"sender": "support@bank-secure.com", "subject": "Verify your account", "urgency_score": 5},
#     {"sender": "hack@evil.com", "subject": "URGENT: Click now", "urgency_score": 8},
# ]
# scan_email(emails)


                






