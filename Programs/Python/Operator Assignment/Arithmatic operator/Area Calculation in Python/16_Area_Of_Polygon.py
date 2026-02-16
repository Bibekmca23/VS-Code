# 16. **Area of Polygon (User enters number of sides &amp; side length)**
# Use formula for regular polygon.

import math

# Input from user
print("\n** Sides must be equal or Greaterthan 3 **")
n = int(input("Enter number of sides: "))
a = float(input("Enter side length: "))

# Area calculation
area = (n * (a ** 2)) / (4 * math.tan(math.pi / n))

# Output
print("Area of regular polygon:", area)




# import math

# # Input from user
# n = int(input("Enter number of sides of the polygon: "))
# s = float(input("Enter length of each side: "))

# if n < 3 or s <= 0:
#     print("A polygon must have at least 3 sides and positive side length!")
# else:
#     area = (n * s**2) / (4 * math.tan(math.pi / n))
#     print("Area of the polygon is:", area)