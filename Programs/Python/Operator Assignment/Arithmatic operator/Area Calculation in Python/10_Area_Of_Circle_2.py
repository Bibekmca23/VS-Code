# 10. **Area of a Circle (User chooses π)**
# Ask user: “Enter π as 3.14 or 22/7”, then compute.

radius = float(input("Enter the radius of the circle: "))
pi_choice = input("Enter π as 3.14 or 22/7: ")

if pi_choice == "3.14":
    pi = 3.14
elif pi_choice == "22/7":
    pi = 22 / 7
else:
    print("Invalid choice for π. Please enter either 3.14 or 22/7.")
    exit()

area = pi * radius * radius
print("Area of Circle: ", area)