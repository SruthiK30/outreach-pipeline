# stage1_ocean.py
import requests
from config import OCEAN_API_KEY

def find_lookalike_companies(seed_domain, limit=10):
    # Ocean.io API requires a paid plan (Professional/Enterprise).
    # For demo purposes, we simulate the lookalike search with known
    # payment/fintech companies similar to stripe.com
    print(f"[Ocean.io] Fetching lookalike companies for: {seed_domain}")

    # Simulated lookalike results — in production this calls Ocean.io API
    lookalikes = {
        "stripe.com": [
            "braintreepayments.com",
            "adyen.com",
            "razorpay.com",
            "paystack.com",
            "paddle.com",
            "chargebee.com",
            "recurly.com",
            "zuora.com",
            "chargify.com",
            "billsby.com"
        ]
    }

    # Try real API first, fall back to simulated data
    try:
        url = "https://api.ocean.io/v2/search/companies"
        headers = {
            "x-api-token": OCEAN_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "size": limit,
            "companiesFilters": {
                "lookalikeDomains": [seed_domain]
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            companies = data.get("companies", [])
            domains = [c["domain"] for c in companies if c.get("domain")]
            if domains:
                print(f"[Ocean.io] Found {len(domains)} lookalike companies via API")
                return domains
    except Exception:
        pass

    # Fallback to simulated data
    domains = lookalikes.get(seed_domain, lookalikes["stripe.com"])[:limit]
    print(f"[Ocean.io] Found {len(domains)} lookalike companies (simulated)")
    return domains