# Webhooks

Receive real-time notifications when events happen in your Kollat account.

---

## Setup

### Register your URL

```bash
POST /api/b2b/webhook/
Content-Type: application/json

{
  "webhook_url": "https://yourapp.com/kollat/events"
}
```

Your endpoint must:

- Accept POST requests
- Return HTTP 200 within 10 seconds
- Handle duplicate deliveries (events may be retried)

---

## Signature verification (recommended)

Generate a signing secret to verify that events come from Kollat:

```bash
POST /api/b2b/webhook/rotate-secret/
```

Response:

```json
{
  "webhook_secret": "a1b2c3d4e5f6..."
}
```

The secret is shown only once. Store it securely.

Every webhook request includes the header:

```
X-Kollat-Signature: sha256=<hmac>
```

### Verify in Python

```python
import hmac
import hashlib

def verify_signature(payload_bytes: bytes, header: str, secret: str) -> bool:
    expected = "sha256=" + hmac.new(
        secret.encode(), payload_bytes, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, header)
```

### Verify in Node.js

```javascript
const crypto = require('crypto');

function verifySignature(payloadBuffer, header, secret) {
  const expected = 'sha256=' + crypto
    .createHmac('sha256', secret)
    .update(payloadBuffer)
    .digest('hex');
  return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(header));
}
```

---

## Events

### Off-ramp (payment orders)

| Event                        | Trigger                                           |
|------------------------------|---------------------------------------------------|
| offramp.comprobante_subido   | Validator uploaded payment proof                  |
| offramp.confirmada           | Employee confirmed receipt, order complete        |
| offramp.reclamada            | Employee disputed the payment                     |
| disputa.resuelta             | Admin resolved a disputed order                   |

### On-ramp (USDT purchases)

| Event              | Trigger                                           |
|--------------------|---------------------------------------------------|
| onramp.tomada      | A validator accepted the buy order                |
| onramp.completada  | Validator confirmed fiat received, USDT released  |
| onramp.expirada    | Order expired with no validator response          |

---

## Payload structure

All events share the same envelope:

```json
{
  "event": "offramp.confirmada",
  "timestamp": "2025-04-09T14:32:00Z",
  "data": {
    "orden_id": 1001,
    "estado": "completada",
    "receptor_id": 42,
    "cantidad_usdt": "150.000000",
    "monto_fiat": "637500.00",
    "moneda_fiat": "COP"
  }
}
```

---

## Retries

If your endpoint returns anything other than 2xx, Kollat will retry:

- After 1 minute
- After 5 minutes
- After 30 minutes

After 3 failed attempts the event is dropped.

---

## Check current config

```bash
GET /api/b2b/webhook/
```

```json
{
  "webhook_url": "https://yourapp.com/kollat/events",
  "secret_activo": true
}
```
