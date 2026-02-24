# Lesson 03: OOP and Virtual Environments

## Learning Objectives
- Define a class with attributes and methods.
- Instantiate objects and call behavior.
- Create and use a Python virtual environment.

## Core Concepts
- `__init__` for object setup.
- Instance methods and `self`.
- Dependency isolation via `venv`.

## Guided Example
```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

## Environment Commands
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Practice Tasks
1. Build a `BankAccount` class with `deposit` and `withdraw`.
2. Activate `.venv` and verify `python -V`.

## Exit Criteria
You can explain why `venv` is required and model simple state with classes.
