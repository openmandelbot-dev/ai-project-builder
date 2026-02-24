# Lesson 08: Script Hardening

## Learning Objectives
- Add defensive checks for user input and file paths.
- Handle network and parsing failures gracefully.
- Improve script reliability for repeated use.

## Core Concepts
- Validation before execution.
- Specific exception handling (`ValueError`, `requests.RequestException`).
- Timeouts, retry options, and predictable error messages.

## Hardening Checklist
- Validate CLI args.
- Fail fast on missing dependencies.
- Add explicit timeout for all HTTP calls.
- Print actionable errors.

## Practice Tasks
1. Add invalid-input handling to one project.
2. Add one failure-path test run per script.

## Exit Criteria
Your scripts are stable on both happy path and common failure paths.
