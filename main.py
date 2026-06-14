# main.py
from stage1_ocean import find_lookalike_companies
from stage2_prospeo import find_decision_makers
from stage3_brevo import send_emails

def run_pipeline(seed_domain):
    print(f"\n Starting pipeline for: {seed_domain}\n")

    # Stage 1 - Find lookalike companies
    print("--- Stage 1: Finding lookalike companies ---")
    domains = find_lookalike_companies(seed_domain)
    if not domains:
        print("No companies found. Exiting.")
        return
    print(f"Domains found: {domains}\n")

    # Stage 2 - Find decision makers and emails
    print("--- Stage 2: Finding decision makers ---")
    contacts = find_decision_makers(domains)
    if not contacts:
        print("No contacts found. Exiting.")
        return

    # Safety checkpoint
    print("\n--- SUMMARY BEFORE SENDING ---")
    for c in contacts:
        print(f"  {c['name']} ({c['title']}) at {c['domain']} → {c['email']}")
    print(f"\nTotal: {len(contacts)} emails ready to send.")

    confirm = input("\nSend emails? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Aborted. No emails sent.")
        return

    # Stage 3 - Send emails
    print("\n--- Stage 3: Sending emails ---")
    send_emails(contacts)
    print("\n Pipeline complete!")

if __name__ == "__main__":
    seed = input("Enter seed domain: ").strip()
    run_pipeline(seed)
