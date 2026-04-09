// Kollat B2B API — Webhook receiver (Node.js / Express)
// Requires: npm install express

const crypto = require("crypto");
const express = require("express");

const app = express();
const WEBHOOK_SECRET = "your_webhook_secret_here";

// Use raw body for signature verification
app.use("/kollat/events", express.raw({ type: "application/json" }));

function verifySignature(payload, header) {
  if (!header) return false;
  const expected =
    "sha256=" +
    crypto.createHmac("sha256", WEBHOOK_SECRET).update(payload).digest("hex");
  return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(header));
}

app.post("/kollat/events", (req, res) => {
  const signature = req.headers["x-kollat-signature"] || "";

  if (!verifySignature(req.body, signature)) {
    return res.status(401).json({ error: "Invalid signature" });
  }

  const event = JSON.parse(req.body);
  handleEvent(event);

  res.json({ ok: true });
});

function handleEvent(event) {
  const { type: eventType, data } = event;

  switch (eventType) {
    case "offramp.confirmada":
      console.log(`Payment confirmed: order #${data.orden_id}`);
      break;
    case "offramp.reclamada":
      console.log(`Payment disputed: order #${data.orden_id} — review required`);
      break;
    case "onramp.completada":
      console.log(`On-ramp completed: order #${data.orden_id}`);
      break;
    case "onramp.expirada":
      console.log(`On-ramp expired: order #${data.orden_id}`);
      break;
    default:
      console.log(`Unhandled event: ${eventType}`);
  }
}

app.listen(8080, () => console.log("Webhook receiver running on :8080"));
