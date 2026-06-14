# Automated Outreach Pipeline

A command-line pipeline that takes a single company domain and automatically finds similar companies, identifies decision-makers, and sends personalized cold outreach emails — end to end, with a manual confirmation step before any email is sent.

## How it works

1. **Find lookalike companies** (Ocean.io) — given a seed domain (e.g. `stripe.com`), finds companies with a similar profile.
2. **Find decision-makers** (Prospeo) — for each company, finds C-suite, VP, and Director-level contacts with verified work emails.
3. **Safety checkpoint** — prints a full summary of every contact found (name, title, company, email) and asks for confirmation before sending.
4. **Send outreach emails** (Brevo) — sends a personalized cold email to each confirmed contact.

> Note: Ocean.io's lookalike API requires a paid plan. When the API isn't accessible, Stage 1 falls back to a curated list of similar companies so the pipeline can still run end to end. Swap in a live Ocean.io call once API access is available.

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `config.example.py` to `config.py` and fill in your own API keys:
   ```bash
   cp config.example.py config.py
   ```
3. Run the pipeline:
   ```bash
   python main.py
   ```
4. Enter a seed domain when prompted, review the contact summary, and type `yes` to send.

## Tech stack

- Python 3
- `requests` for all API calls
- Ocean.io, Prospeo, and Brevo APIs

## Project structure

```
outreach-pipeline/
├── main.py              # orchestrates the full pipeline
├── stage1_ocean.py       # finds lookalike companies
├── stage2_prospeo.py     # finds decision-makers + verified emails
├── stage3_brevo.py       # (Stage 3 merged into Stage 2 — Prospeo returns verified emails)
├── config.example.py     # template for API keys
└── requirements.txt
```
