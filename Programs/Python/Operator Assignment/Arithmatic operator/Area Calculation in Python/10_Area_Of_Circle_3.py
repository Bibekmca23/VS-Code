# 10. **Area of a Circle (User chooses π)**
# Ask user: “Enter π as 3.14 or 22/7”, then compute. (With improvements an upgrade version with error handling)

import math

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def area_calculator():
    while True:
        print("\n--- Area Calculator Menu ---")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Triangle")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            radius = get_positive_float("Enter radius of circle: ")
            area = math.pi * radius ** 2
            print(f"Area of Circle = {area:.2f}")

        elif choice == '2':
            length = get_positive_float("Enter length of rectangle: ")
            width = get_positive_float("Enter width of rectangle: ")
            area = length * width
            print(f"Area of Rectangle = {area:.2f}")

        elif choice == '3':
            side = get_positive_float("Enter side of square: ")
            area = side ** 2
            print(f"Area of Square = {area:.2f}")

        elif choice == '4':
            base = get_positive_float("Enter base of triangle: ")
            height = get_positive_float("Enter height of triangle: ")
            area = 0.5 * base * height
            print(f"Area of Triangle = {area:.2f}")

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1-5.")

# Run the calculator
area_calculator()