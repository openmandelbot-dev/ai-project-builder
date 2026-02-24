# Milestone: Automated Public API Job

## Objective
Deploy a Python script that consumes a public API and runs automatically.

## Implementation in This Repo
- Script: `weeks/week-2/scripts/milestone_api_job.py`
- Workflow: `.github/workflows/milestone-api-job.yml`
- Output artifact: `milestone-output.json`

## Validation Checklist
- Workflow runs from manual trigger and schedule.
- Script fails fast on HTTP errors.
- Output JSON artifact is uploaded from each run.
- Timestamp is included for observability.

## Demo API
Use Open-Meteo (`https://api.open-meteo.com`) to avoid API keys.
