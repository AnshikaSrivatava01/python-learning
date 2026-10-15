def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        return fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 2)[-1]]

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Invalid input")  
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(n)[i])