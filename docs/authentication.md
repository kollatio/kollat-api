# Authentication

Every request to the Kollat B2B API requires your company's API Key.

```
Authorization: Api-Key klt_your_key_here
```


Getting your API Key

1. Create your account at kollat.io
2. Register your company in the dashboard
3. Accept the Terms and Conditions
4. Go to Settings → API Keys → Create

The full key is shown only once. Store it securely — it cannot be retrieved again.


Key rules

- Each company can have multiple active API Keys
- Keys do not expire but can be revoked at any time
- Revoking a key is immediate — all requests using it fail instantly
- After revoking, create a new key from the dashboard

Revoke a key:

```bash
DELETE /api/b2b/api-keys/{key_id}/revoke/
Authorization: Api-Key klt_your_key_here
```

List your keys:

```bash
GET /api/b2b/api-keys/
Authorization: Api-Key klt_your_key_here
```


Rate limiting

Requests are rate-limited per API Key. If you exceed the limit:

```json
HTTP 429 Too Many Requests
{ "detail": "Request was throttled." }
```

Contact support if you need higher limits.


Error codes

401 — Missing or invalid API Key
403 — Valid key but insufficient permissions
429 — Rate limit exceeded
