# 12. **Area of Circle with Math Library**
# Use `math.pi` instead of constant 3.14.

import math

radius = float(input("Enter radius: "))
area = math.pi * math.pow(radius, 2)
print(f"Area of Circle = {area:.2f}") 