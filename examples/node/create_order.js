// Kollat B2B API — Create a payment order (Node.js)
// Requires: npm install node-fetch  (or use built-in fetch in Node 18+)

const API_KEY = "klt_your_key_here";
const BASE_URL = "https://www.kollat.io/api/b2b";

const headers = {
  Authorization: `Api-Key ${API_KEY}`,
  "Content-Type": "application/json",
};

async function getRate(currency) {
  const res = await fetch(`${BASE_URL}/rates/?currency=${currency}`, { headers });
  if (!res.ok) throw new Error(`getRate failed: ${res.status}`);
  return res.json();
}

async function createOrder(empleadoId, cantidadUsdt) {
  const res = await fetch(`${BASE_URL}/orders/create/`, {
    method: "POST",
    headers,
    body: JSON.stringify({
      receptor_type: "empleado",
      receptor_id: empleadoId,
      cantidad_usdt: cantidadUsdt,
    }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(JSON.stringify(err));
  }
  return res.json();
}

(async () => {
  const rate = await getRate("COP");
  console.log(`Current rate: 1 USDT = ${rate.tasa} ${rate.moneda}`);

  const order = await createOrder(42, 150.0);
  console.log(`Order created: #${order.orden_id} — ${order.estado}`);
  console.log(`  Recipient will receive: ${order.monto_fiat} ${order.moneda_fiat}`);
})();
