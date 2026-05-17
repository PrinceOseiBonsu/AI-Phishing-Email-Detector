# gmail_integration.py
# Gmail API Integration for AI Phishing Detector

import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIALS_FILE = 'credentials.json'

def get_gmail_flow():
    flow = Flow.from_client_secrets_file(
        CREDENTIALS_FILE,
        scopes=SCOPES,
        redirect_uri='http://localhost:5000/gmail/callback'
    )
    flow.code_verifier = None
    return flow

def get_gmail_service(token_data):
    creds = Credentials(
        token=token_data.get('token'),
        refresh_token=token_data.get('refresh_token'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=token_data.get('client_id'),
        client_secret=token_data.get('client_secret'),
        scopes=SCOPES
    )
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_recent_emails(service, max_results=10):
    results = service.users().messages().list(
        userId='me',
        maxResults=max_results,
        labelIds=['INBOX']
    ).execute()

    messages = results.get('messages', [])
    emails = []

    for message in messages:
        msg = service.users().messages().get(
            userId='me',
            id=message['id'],
            format='full'
        ).execute()

        headers = msg['payload']['headers']
        subject = next((h['value'] for h in headers
                       if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers
                      if h['name'] == 'From'), 'Unknown')

        body = ""
        if 'parts' in msg['payload']:
            for part in msg['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    if 'data' in part['body']:
                        body = base64.urlsafe_b64decode(
                            part['body']['data']).decode('utf-8')
                        break
        elif 'body' in msg['payload']:
            if 'data' in msg['payload']['body']:
                body = base64.urlsafe_b64decode(
                    msg['payload']['body']['data']).decode('utf-8')

        emails.append({
            'id': message['id'],
            'subject': subject,
            'sender': sender,
            'body': body[:1000]
        })

    return emails