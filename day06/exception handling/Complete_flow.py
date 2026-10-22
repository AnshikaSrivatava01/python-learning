def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."   
    else:
        print(f"Calculation succeeded. The result is: {result}")
    finally:
        print("Execution completed.") 

print(divide_numbers(10, 2))
print(divide_numbers(10,0))           