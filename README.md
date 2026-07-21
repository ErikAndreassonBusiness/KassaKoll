# Kassakollen – Fortnox Integration

> **Automatiserad likviditetsanalys och kassaflödesprognos direkt inuti Fortnox.**

**Kassakollen** är en inbäddad Fortnox-app (embedded app) utvecklad för småföretagare och mikroföretag. Appen hämtar rådata från Fortnox via deras API och översätter den till en tydlig, visuell 30-dagars likviditetsprognos.

Kunden får ett direkt svar på frågan: _"Finns det tillräckligt med kassa i företaget för att betala alla räkningar, skatter och löner de närmsta 30 dagarna?"_

---

## Funktioner

- **Realtidsöversikt av kassan:** Läser av aktuellt saldo på likvida konton (Konto 19XX).
- **30-dagars Likviditetsprognos:** Beräknar kassaflödet framåt genom att ställa tillgänglig kassa + kommande inbetalningar (kundfakturor) mot kommande utbetalningar (leverantörsfakturor).
- **Proaktiva Varningssignaler:** Tydlig visuell status (Grön / Gul / Röd) om kassan understiger inställda tröskelvärden eller om ett underskott förutspås ett visst datum.
- **Sömlös Fortnox-upplevelse:** Körs som en inbäddad app (embedded app / iFrame) direkt inuti Fortnox gränssnitt med Single Sign-On (SSO).

---

## Systemarkitektur

Projektet är uppbyggt av en frikopplad arkitektur med en Python-backend och en lättviktig webb-frontend:

```text
┌────────────────────────────────────────────────────────┐
│                  Fortnox Gränssnitt                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Frontend (Embedded iFrame / Dashboard)          │  │
│  │  - HTML / CSS / JavaScript                       │  │
│  │  - Chart.js (Visualisering & Grafer)             │  │
│  └─────────────────────────┬────────────────────────┘  │
└────────────────────────────┼───────────────────────────┘
                             │ API-anrop (JSON)
                             ▼
┌────────────────────────────────────────────────────────┐
│                  Backend (FastAPI)                     │
│  - OAuth 2.0 & Token Refresh Manager                   │
│  - Likviditetsmotor (Kassa + Inbet - Utbet)            │
│  - Database Manager (Tokens & Inställningar)           │
└────────────────────────────┬───────────────────────────┘
                             │ REST API (HTTPS)
                             ▼
┌────────────────────────────────────────────────────────┐
│                     Fortnox API                        │
│  - /3/financialyears & /3/accounts (Konto 19XX)        │
│  - /3/invoices (Obetalda kundfakturor)                 │
│  - /3/supplierinvoices (Obetalda leverantörsfakturor)  │
└────────────────────────────────────────────────────────┘
```

---

## 📁 Mappsturktur

```text
KassaKoll/
├── app/
│   ├── client/
│   │   ├── static/          # CSS, JavaScript, Images, etc.
│   │   └── templates/       # HTML templates (Jinja2)
│   └── server/
│       └── __init__.py      # FastAPI application setup (`app = FastAPI()`)
├── .gitignore
├── .python-version
├── pyproject.toml           # Project dependencies & metadata
├── README.md
├── run.py                   # Main entry point (`uv run run.py`)
└── uv.lock                  # Deterministic lockfile managed by uv
```

---

## UV Workfolw Guide

### Set Up Environment

Install all dependencies from `uv.lock` into your virtual environment:

```bash
uv sync
```

### Run the Development Server

Start the FastAPI app with hot-reloading enabled:

```bash
uv run run.py
```

---

## `uv` Complete Workflow Cheat Sheet

This project relies on **`uv`** for managing dependencies, virtual environments, and python scripts.

### Adding Dependencies

To install a new production package and automatically update `pyproject.toml` and `uv.lock`:

```bash
uv add <package_name>
```

For development-only tools (testing, formatting, linters):

```bash
uv add --dev <package_name>
```

### Removing Dependencies

To uninstall a package and clean up project files:

```bash
uv remove <package_name>
```

### Updating Dependencies

To bump packages to their latest compatible versions and sync:

```bash
uv lock --upgrade
uv sync
```

### Reset Environment

If you ever need to perform a clean reinstall of your `.venv`:

```bash
rm -rf .venv
uv sync
```
