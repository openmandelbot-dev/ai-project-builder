# Lesson 04: REST APIs and JSON Parsing

## Learning Objectives
- Call a REST endpoint with `requests`.
- Validate HTTP responses.
- Extract fields from nested JSON.

## Core Concepts
- HTTP `GET`, status codes, and timeouts.
- `response.raise_for_status()` for fail-fast behavior.
- Safe extraction with `dict.get()`.

## Guided Example
```python
import requests

resp = requests.get("https://api.open-meteo.com/v1/forecast?latitude=37.77&longitude=-122.41&current=temperature_2m", timeout=10)
resp.raise_for_status()
data = resp.json()
print(data.get("current", {}).get("temperature_2m"))
```

## Practice Tasks
1. Fetch API data and print 2 selected keys.
2. Handle missing keys with defaults.
3. Add a timeout and error message path.

## Exit Criteria
You can build a CLI script that calls an API and prints clean output.
