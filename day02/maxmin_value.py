l = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    el = int(input(f"Enter element {i + 1}: "))
    l.append(el)

print(f"The maximum value is: {max(l)}")
print(f"The minimum value is: {min(l)}")