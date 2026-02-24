"""Milestone job: consume public API and write JSON output."""

import json
from datetime import datetime, timezone

import requests


def run() -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=37.7749&longitude=-122.4194&current=temperature_2m,weather_code"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    payload = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "open-meteo",
        "data": response.json(),
    }

    with open("milestone-output.json", "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)

    return payload


if __name__ == "__main__":
    result = run()
    print("Milestone job completed.")
    print(result["fetched_at_utc"])
