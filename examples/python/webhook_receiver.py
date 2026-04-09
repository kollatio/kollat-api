"""
Kollat B2B API — Webhook receiver example (Python / Flask)
Requires: pip install flask
"""

import hashlib
import hmac

from flask import Flask, abort, jsonify, request

app = Flask(__name__)

WEBHOOK_SECRET = "your_webhook_secret_here"


def verify_signature(payload: bytes, header: str) -> bool:
    if not header:
        return False
    expected = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, header)


@app.route("/kollat/events", methods=["POST"])
def kollat_webhook():
    signature = request.headers.get("X-Kollat-Signature", "")

    if not verify_signature(request.data, signature):
        abort(401, "Invalid signature")

    event = request.json
    handle_event(event)

    return jsonify({"ok": True}), 200


def handle_event(event: dict):
    event_type = event.get("event")
    data = event.get("data", {})

    if event_type == "offramp.confirmada":
        orden_id = data["orden_id"]
        print(f"Payment confirmed: order #{orden_id}")

    elif event_type == "offramp.reclamada":
        orden_id = data["orden_id"]
        print(f"Payment disputed: order #{orden_id} — review required")

    elif event_type == "onramp.completada":
        orden_id = data["orden_id"]
        print(f"On-ramp completed: order #{orden_id}")

    elif event_type == "onramp.expirada":
        orden_id = data["orden_id"]
        print(f"On-ramp expired: order #{orden_id} — recreate if needed")

    else:
        print(f"Unhandled event: {event_type}")


if __name__ == "__main__":
    app.run(port=8080)
