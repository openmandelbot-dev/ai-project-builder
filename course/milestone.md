# Milestone: Automated Public API Script

## Objective
Deploy a Python script that calls a public API and runs automatically on a schedule.

## Included Implementation
- Script: `scripts/milestone_api_job.py`
- Scheduled runner: `.github/workflows/milestone-api-job.yml`
- Output artifact: `milestone-output.json`

## Validation Checklist
- Workflow runs successfully on schedule.
- Script handles HTTP failures gracefully.
- Output file is generated and uploaded as an artifact.

## Suggested Demo
Use [Open-Meteo](https://open-meteo.com/) as a free public API to fetch weather data.
