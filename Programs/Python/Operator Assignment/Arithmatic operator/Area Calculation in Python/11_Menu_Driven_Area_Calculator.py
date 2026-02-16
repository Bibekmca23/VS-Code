# 11. **Menu-Driven Area Calculator**
# Show menu of shapes; compute area based on user choice.


# while True:
#     print("\n--- Area Calculator Menu ---")
#     print("1. Area of Circle")
#     print("2. Area of Rectangle")
#     print("3. Area of Triangle")
#     print("4. Area of Square")
#     print("5. Exit")

#     choice = input("\nChoose a shape (1-5): ")

#     match choice:
#         case "1":
#             radius = float(input("Enter the radius of the circle: "))
#             pi_choice = input("Enter π as 3.14 or 22/7: ")

#             match pi_choice:
#                 case "3.14":
#                     pi = 3.14
#                 case "22/7":
#                     pi = 22 / 7
#                 case _:
#                     print("Invalid π choice. Try again.")
#                     continue

#             area = pi * radius * radius
#             print("Area of Circle:", area)

#         case "2":
#             length = float(input("Enter the length of the rectangle: "))
#             width = float(input("Enter the width of the rectangle: "))
#             area = length * width
#             print("Area of Rectangle:", area)

#         case "3":
#             base = float(input("Enter the base of the triangle: "))
#             height = float(input("Enter the height of the triangle: "))
#             area = 0.5 * base * height
#             print("Area of Triangle:", area)

#         case "4":
#             side = float(input("Enter the side of the square: "))
#             area = side * side
#             print("Area of Square:", area)

#         case "5":
#             print("Exiting the program... \n...\n...\n\nGoodbye!!")
#             break

#         case _:
#             print("Invalid choice. Please select a valid option.")



























# import math
# while True:
#     print("\n--- Area Calculator Menu ---\n")
#     print("1. Area of Circle")
#     print("2. Area of Rectangle")
#     print("3. Area of Triangle")
#     print("4. Area of Square")
#     print("5. Exit")

#     choice = input("\nChoose a shape (1-5): ")

#     if choice == "1":
#         radius = float(input("Enter the radius of the circle: "))
#         pi_choice = input("Enter π as (3.14 or 22/7): ")

#         if pi_choice == "3.14":
#             pi = 3.14
#         elif pi_choice == "22/7":
#             pi = 22 / 7
#         else:
#             print("Invalid choice for π. Please enter either 3.14 or 22/7.")

#         area = pi * radius * radius
#         print("Area of Circle: ", area)

#     elif choice == "2":
#         length = float(input("Enter the length of the rectangle: "))
#         width = float(input("Enter the width of the rectangle: "))
#         area = length * width
#         print("Area of Rectangle: ", area)

#     elif choice == "3":
#         base = float(input("Enter the base of the triangle: "))
#         height = float(input("Enter the height of the triangle: "))
#         area = 0.5 * base * height
#         print("Area of Triangle: ", area)

#     elif choice == "4":
#         side = float(input("Enter the side of the square: "))
#         area = side * side
#         print("Area of Square: ", area)
        
#     elif choice == "5":
#         print("Exiting the program...... \nGoodbye!")
#         exit()

#     else:
#         print("Invalid choice. Please select a valid option from the menu.")
