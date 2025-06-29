import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

class GmailMessagesRetriever:
    @staticmethod
    def getCreds():
        '''
        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.
        '''
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds
    
    def __init__(self):
         # Call the Gmail API
        creds = self.getCreds()
        service = build("gmail", "v1", credentials=creds)

        results = service.users().messages().list(
            userId="me",
            q="is:unread",
            maxResults=5
            ).execute()
        messages = results.get("messages", [])

        if not messages:
            print("Нет писем")
        else:
            print(f"Найдено {len(messages)} непрочитанных писем:")
            
            for msg in messages:
                message = service.users().messages().get(
                    userId="me",
                    id=msg["id"],
                    format="full",
                    metadataHeaders=["Subject", "From"]
                ).execute()

                headers = message["payload"]["headers"]
                subject = next(h["value"] for h in headers if h["name"] == "Subject")
                sender = next(h["value"] for h in headers if h["name"] == "From")
                print(f"Тема: {subject}\nОт: {sender}")

                parts = message["payload"]["parts"]
                for part in parts:
                    if part["mimeType"] == "text/plain":
                        text_data = part["body"]["data"]  # Данные в base64
                        text = base64.urlsafe_b64decode(text_data).decode("utf-8")
                        print("Текст письма:", text)

GmailMessagesRetriever()
