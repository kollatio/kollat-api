# Kollat B2B API

Pay anyone in Latin America from your USDT balance. Recipients get local currency in their bank account in hours, not days. No crypto wallets required. No local banking relationships needed.

Base URL: `https://www.kollat.io/api/b2b/`
Documentation: `https://www.kollat.io/api/b2b/docs/`

---

Quick Example

```bash
curl -X POST https://www.kollat.io/api/b2b/orders/create/ \
  -H "Authorization: Api-Key klt_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"recipient_id": 42, "amount_usdt": 150, "country": "VE"}'
```

See [docs/quickstart.md](docs/quickstart.md) for full integration.

---

What It Does

Your platform holds USDT. Kollat converts and delivers local currency to any bank account in Latin America with one API call.

You send: USDT via API
Recipient gets: Local fiat in their bank account
Time: 0.5–4 hours
Cost: Under 2%

---

Use Cases

Remote-First Companies
Problem: High fees and delays paying LatAm contractors
Solution: Payroll in hours, under 2% commission, no wire transfers


iGaming and Betting Platforms
Problem: Player withdrawals take 5+ days via SWIFT, Venezuela and Colombia are hard to pay
Solution: Process withdrawals in 2 hours, reach markets others cannot


Web3 and P2E Platforms
Problem: Users earn USDT but do not know how to cash out
Solution: Automatic conversion to local fiat, zero crypto knowledge required

Marketplaces
Problem: Need multiple local banking relationships across LatAm
Solution: One USDT balance, payouts to 5 countries from a single integration

On-Ramp
Problem: Hard to acquire USDT with local currency
Solution: Send local fiat via bank transfer, receive USDT

---

How It Works

1. Register recipient via API — name, document, country
2. Recipient completes KYC and adds bank account
3. Deposit USDT to your Kollat wallet
4. Create payment order — Kollat handles conversion and payout

Certified validators execute local bank transfers. You receive webhook confirmations when funds are delivered.

---

Active Countries

Venezuela · Colombia · Chile · Panama · Argentina

Check available countries at runtime: `GET /countries/`

---

Supported Networks

BEP-20 · Arbitrum 

---

Why Kollat

Speed: Hours not days using local bank rails
Cost: Under 2% flat fee, no hidden FX spreads
Coverage: Hard-to-reach markets traditional providers skip
Simplicity: One integration, multiple countries, multiple networks
Compliance: KYC handled, full audit trail, digital receipts

---

Endpoints

`POST /recipients/register/` — Register payment recipients
`POST /orders/create/` — Create single payment order
`POST /batch/create/` — Send payments to multiple recipients
`POST /onramp/orders/create/` — Acquire USDT via local bank transfer
`GET /rates/` — Live USDT to local currency exchange rates
`GET /deposits/` — Check your USDT balance
`GET /movements/` — Full transaction history
`POST /webhook/` — Configure real-time notifications
`GET /receipts/` — Generate digital receipts in local currency

---

Authentication

All requests require API Key in header:

```
Authorization: Api-Key klt_your_key_here
```

Get your API Key from the dashboard or via `POST /api-keys/create/`

---

Resources

[Authentication guide](docs/authentication.md)
[Quickstart](docs/quickstart.md)
[API reference](https://www.kollat.io/api/b2b/docs/)
[Webhooks](docs/webhooks.md)
[Code examples — Python](examples/python/)
[Code examples — Node.js](examples/node/)
[Code examples — cURL](examples/curl/examples.sh)

---

Get Access

Request API keys at kollat.io/b2b or email andresjose.jimenez@kollat.io
