"""
Kollat B2B API — Create a payment order (Python)
Requires: pip install requests
"""

import requests

API_KEY = "klt_your_key_here"
BASE_URL = "https://www.kollat.io/api/b2b"

headers = {
    "Authorization": f"Api-Key {API_KEY}",
    "Content-Type": "application/json",
}


def get_rate(currency: str) -> dict:
    r = requests.get(f"{BASE_URL}/rates/", params={"currency": currency}, headers=headers)
    r.raise_for_status()
    return r.json()


def create_order(empleado_id: int, cantidad_usdt: float) -> dict:
    payload = {
        "receptor_type": "empleado",
        "receptor_id": empleado_id,
        "cantidad_usdt": cantidad_usdt,
    }
    r = requests.post(f"{BASE_URL}/orders/create/", json=payload, headers=headers)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    rate = get_rate("COP")
    print(f"Current rate: 1 USDT = {rate['tasa']} {rate['moneda']}")

    order = create_order(empleado_id=42, cantidad_usdt=150.00)
    print(f"Order created: #{order['orden_id']} — {order['estado']}")
    print(f"  Recipient will receive: {order['monto_fiat']} {order['moneda_fiat']}")
