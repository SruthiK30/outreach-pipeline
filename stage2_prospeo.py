# stage2_prospeo.py
import requests
import time
from config import PROSPEO_API_KEY

def find_decision_makers(domains):
    url = "https://api.prospeo.io/search-person"
    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }
    contacts = []

    for domain in domains[:5]:
        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [domain]
                    }
                },
                "person_seniority": {
                    "include": ["C-Suite", "Vice President", "Director"]
                }
            }
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])

            for result in results:
                person = result.get("person", {})
                email_obj = person.get("email", {})
                email_status = email_obj.get("status", "")
                email_value = email_obj.get("email", "")

                # use email if verified (even if masked for demo)
                if email_status == "VERIFIED" and email_value:
                    contacts.append({
                        "domain": domain,
                        "name": person.get("full_name", ""),
                        "email": email_value,
                        "title": person.get("current_job_title", ""),
                        "linkedin": person.get("linkedin_url", "")
                    })

        except Exception as e:
            print(f"[Prospeo] Error for {domain}: {e}")

        time.sleep(2)

    print(f"[Prospeo] Found {len(contacts)} contacts with verified emails")
    return contacts