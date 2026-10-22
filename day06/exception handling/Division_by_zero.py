def safe_calculator(a, b, operation):
    try:
        if operation == '/':
            result = a / b
        elif operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        else:
            raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(safe_calculator(10, 0, '/')) 
print(safe_calculator(10, 2, '/'))