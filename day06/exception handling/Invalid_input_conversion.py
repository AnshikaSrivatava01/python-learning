user_input = input("Enter a number: ")
try:
    num = int(user_input)
    print(f"Valid integer entered: {num}")
except ValueError:
    print(f"Error: '{user_input}' is not a valid integer.")    