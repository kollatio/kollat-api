# Quickstart

Send your first payment in 5 steps.

All examples use:

```
Authorization: Api-Key klt_your_key_here
```


Step 1 — Get your API Key

1. Create your account at kollat.io
2. Register your company in the dashboard
3. Accept the Terms and Conditions
4. Go to Settings → API Keys → Create → copy your key

See [authentication.md](authentication.md) for key management details.


Step 2 — Check available countries and rates

```bash
GET /api/b2b/countries/
```

```bash
GET /api/b2b/rates/?currency=COP
```

Response:

```json
{
  "moneda": "COP",
  "tasa": 3550.00,
  "pais": "Colombia",
  "codigo_iso": "CO"
}
```


Step 3 — Register a recipient

```bash
POST /api/b2b/recipients/register/
Authorization: Api-Key klt_your_key_here
Content-Type: application/json

{
  "email": "juan.perez@email.com",
  "username": "juan.perez",
  "first_name": "Juan",
  "last_name": "Perez",
  "documento_identidad": "1234567890",
  "tipo_documento": "CC",
  "pais": "CO"
}
```

Response:

```json
{
  "empleado_id": 42,
  "kyc_url": "https://verify.didit.me/session/abc123",
  "mensaje": "Recipient registered. Share the kyc_url so they can complete identity verification."
}
```

The recipient must:

1. Complete KYC via the provided link
2. Add their bank account

You cannot send payments until both steps are completed.

Check KYC status:

```bash
GET /api/b2b/recipients/42/kyc/status/
Authorization: Api-Key klt_your_key_here
```

```json
{
  "kyc_completado": true,
  "estado": "approved",
  "tiene_cuenta_bancaria": true
}
```


Step 4 — Deposit USDT

Get your deposit address:

```bash
GET /api/b2b/wallets/
Authorization: Api-Key klt_your_key_here
```

```json
{
  "direccion_usdt": "0x1234abc...",
  "red": "BEP20",
  "saldo_disponible": "0.000000"
}
```

Send USDT to that address, then register the transaction:

```bash
POST /api/b2b/deposits/submit/
Authorization: Api-Key klt_your_key_here
Content-Type: application/json

{
  "tx_hash": "0x1234abc...",
  "cantidad_usdt": "500.00"
}
```

Supported networks: BEP-20 · Arbitrum · Solana · Tron


Step 5 — Create a payment order

```bash
POST /api/b2b/orders/create/
Authorization: Api-Key klt_your_key_here
Content-Type: application/json

{
  "recipient_id": 42,
  "amount_usdt": 150.00
}
```

Response:

```json
{
  "orden_id": 1001,
  "estado": "pending",
  "recipient": "Juan Perez",
  "amount_usdt": "150.000000",
  "monto_fiat": "637500.00",
  "moneda_fiat": "COP",
  "tasa_usada": "4250.00"
}
```


Batch payments

Send to multiple recipients at once:

```bash
POST /api/b2b/batch/create/
Authorization: Api-Key klt_your_key_here
Content-Type: application/json

{
  "nombre": "payroll april 2026",
  "items": [
    { "empleado_id": 42, "amount_usdt": 150.00 },
    { "empleado_id": 43, "amount_usdt": 200.00 },
    { "empleado_id": 44, "amount_usdt": 175.00 }
  ]
}
```


What happens after an order is created

1. Kollat assigns a certified validator in the recipient's country
2. Validator executes the local bank transfer
3. Recipient receives local currency in their bank account
4. Order status updates to completed

Track status: `GET /api/b2b/orders/`
Real-time updates: [webhooks](webhooks.md)
