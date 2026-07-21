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
