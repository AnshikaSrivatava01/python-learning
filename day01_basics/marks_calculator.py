def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Error: Division by zero is undefined."
    return a / b, None

def modulo(a, b):
    if b == 0:
        return None, "Error: Modulo by zero is undefined."
    return a % b, None

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_calculator():
    while True:
        print("\n=== CALCULATOR MENU ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("Exiting calculator")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Select an option from 1 to 6.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2):.2f}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2):.2f}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2):.2f}")
        elif choice == "4":
            result, error = divide(num1, num2)
            if error:
                print(error)
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")
        elif choice == "5":
            result, error = modulo(num1, num2)
            if error:
                print(error)
            else:
                print(f"Result: {num1} % {num2} = {result:.2f}")

if __name__ == "__main__":
    run_calculator()