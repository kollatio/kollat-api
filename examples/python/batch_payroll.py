"""
Kollat B2B API — Batch payroll run (Python)
Requires: pip install requests
"""

import requests

API_KEY = "klt_your_key_here"
BASE_URL = "https://www.kollat.io/api/b2b"

headers = {
    "Authorization": f"Api-Key {API_KEY}",
    "Content-Type": "application/json",
}


def create_payroll_run(nombre: str, employees: list[dict]) -> dict:
    """
    employees: list of {"empleado_id": int, "cantidad_usdt": float}
    """
    payload = {
        "nombre": nombre,
        "items": employees,
    }
    r = requests.post(f"{BASE_URL}/batch/create/", json=payload, headers=headers)
    r.raise_for_status()
    return r.json()


def get_payroll_status(corrida_id: int) -> dict:
    r = requests.get(f"{BASE_URL}/batch/{corrida_id}/", headers=headers)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    employees = [
        {"empleado_id": 42, "cantidad_usdt": 150.00},
        {"empleado_id": 43, "cantidad_usdt": 200.00},
        {"empleado_id": 44, "cantidad_usdt": 175.50},
    ]

    run = create_payroll_run("Payroll April 2026", employees)
    corrida_id = run["corrida_id"]
    print(f"Payroll run created: #{corrida_id}")
    print(f"  Total USDT: {run['total_usdt']}")
    print(f"  Orders: {run['total_ordenes']}")

    status = get_payroll_status(corrida_id)
    print(f"  Status: {status['estado']}")
