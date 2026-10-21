import math

number = 5

# Square root
sqrt_val = math.isqrt(number) if number.is_integer() else math.sqrt(number)
print(f"Square root of 25: {math.sqrt(25)}")

# Factorial
print(f"Factorial of {number}: {math.factorial(number)}")

# Power (base^exponent)
print(f"{number} raised to the power 3: {math.pow(number, 3)}")