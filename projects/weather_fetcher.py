"""Weather fetcher using Open-Meteo public API."""

import argparse
import requests


def fetch_weather(latitude: float, longitude: float) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch weather from Open-Meteo.")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")
    args = parser.parse_args()

    data = fetch_weather(args.lat, args.lon)
    current = data.get("current", {})
    temperature = current.get("temperature_2m")
    code = current.get("weather_code")

    print(f"Temperature: {temperature}°C")
    print(f"Weather code: {code}")


if __name__ == "__main__":
    main()
