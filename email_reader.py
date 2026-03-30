# email_reader.py
import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def fetch_emails():
    emails = []

    try:
        print("Connecting to Gmail...")
        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        print("Logging in...")
        mail.login(EMAIL, PASSWORD)

        print("Selecting inbox...")
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")

        mail_ids = messages[0].split()

        for i in mail_ids[-5:]:
            status, msg_data = mail.fetch(i, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = msg["Subject"]
                    emails.append(subject)

        mail.logout()

    except Exception as e:
        print("🔥 FULL ERROR:", str(e))
        return ["ERROR_CONNECTION_FAILED"]

    return emails

    for num in messages[0].split():
        _, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        subject = msg["subject"] or ""
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()
        emails.append(subject + " " + body)
    return emails