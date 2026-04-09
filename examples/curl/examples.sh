#!/bin/bash
# Kollat B2B API - cURL examples

API_KEY="klt_your_key_here"
BASE="https://www.kollat.io/api/b2b"

# Countries and rates

# List active countries
curl -s "$BASE/countries/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Get exchange rate for Colombia
curl -s "$BASE/rates/?currency=COP" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Recipients

# Register an employee
curl -s -X POST "$BASE/recipients/register/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan.perez@email.com",
    "username": "juan.perez",
    "first_name": "Juan",
    "last_name": "Perez",
    "documento_identidad": "1234567890",
    "tipo_documento": "CC",
    "pais": "CO"
  }' | jq

# Check KYC status
curl -s "$BASE/recipients/42/kyc/status/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# List all recipients
curl -s "$BASE/recipients/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Wallet and deposits

# Get your USDT deposit address
curl -s "$BASE/wallets/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Notify a USDT deposit
curl -s -X POST "$BASE/deposits/submit/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "tx_hash": "abc123def456...",
    "cantidad_usdt": "500.00"
  }' | jq

# Payment orders

# Single payment order
curl -s -X POST "$BASE/orders/create/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "receptor_type": "empleado",
    "receptor_id": 42,
    "cantidad_usdt": 150.00
  }' | jq

# Batch payment (multiple employees)
curl -s -X POST "$BASE/orders/create/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "42": 150.00,
    "43": 200.00,
    "44": 175.00
  }' | jq

# List payment orders
curl -s "$BASE/orders/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Payroll batch

# Create a named payroll run
curl -s -X POST "$BASE/batch/create/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Payroll April 2026",
    "items": [
      { "empleado_id": 42, "cantidad_usdt": 150.00 },
      { "empleado_id": 43, "cantidad_usdt": 200.00 }
    ]
  }' | jq

# Webhooks

# Register webhook URL
curl -s -X POST "$BASE/webhook/" \
  -H "Authorization: Api-Key $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "webhook_url": "https://yourapp.com/kollat/events" }' | jq

# Rotate signing secret
curl -s -X POST "$BASE/webhook/rotate-secret/" \
  -H "Authorization: Api-Key $API_KEY" | jq

# Movements

# Get transaction history
curl -s "$BASE/movements/" \
  -H "Authorization: Api-Key $API_KEY" | jq
