import math
from unittest import case

def calculate_area(shape):
    if shape == "circle" :
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        return area
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        return area
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        return area 
    else:
        return None

while True:
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        area = calculate_area("circle")
        print(f"The area of the circle is: {area:.2f}")         
    elif choice == "2":
        area = calculate_area("rectangle")
        print(f"The area of the rectangle is: {area:.2f}")  
    elif choice == "3":    
        area = calculate_area("triangle")
        print(f"The area of the triangle is: {area:.2f}")
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")