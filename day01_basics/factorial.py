def fact(x):
    z = 1
    for i in range(1, x + 1):
        z = z * i
    return z

n=int(input("Enter a number: "))
print("The factorial of", n, "is", fact(n))