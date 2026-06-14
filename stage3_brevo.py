# stage3_brevo.py
import requests
from config import BREVO_API_KEY, SENDER_NAME, SENDER_EMAIL

def send_emails(contacts):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "api-key": BREVO_API_KEY,
        "Content-Type": "application/json"
    }

    for contact in contacts:
        first_name = contact['name'].split()[0] if contact['name'] else "there"
        subject = f"Quick question, {first_name}"
        body = f"""Hi {first_name},

I came across {contact['domain']} and was impressed by what your team is building.

We have been helping similar companies streamline their outreach and close more deals in less time. I would love to show you how we can do the same for {contact['domain']}.

Would a quick 15-minute call this week work for you?

Best regards,
{SENDER_NAME}"""

        payload = {
            "sender": {"name": SENDER_NAME, "email": SENDER_EMAIL},
            "to": [{"email": contact["email"], "name": contact["name"]}],
            "subject": subject,
            "textContent": body
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"[Brevo] Email sent to {contact['name']} <{contact['email']}>")
        except Exception as e:
            print(f"[Brevo] Failed for {contact['name']}: {e}")