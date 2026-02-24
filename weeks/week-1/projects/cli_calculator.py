"""Interactive CLI calculator for core Python practice."""

def calculate(a: float, b: float, op: str) -> float:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError(f"Unsupported operator: {op}")


def main() -> None:
    print("CLI Calculator (+, -, *, /). Type q to quit.")
    while True:
        left = input("First number (or q): ").strip()
        if left.lower() == "q":
            break

        right = input("Second number: ").strip()
        op = input("Operator (+ - * /): ").strip()

        try:
            a = float(left)
            b = float(right)
            result = calculate(a, b, op)
            print(f"Result: {result}")
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
