# 8. **Area of a Isosceles Triangle**
# Input equal sides and base; use suitable formula.

import math
a = float(input("Enter length of equal sides of isosceles triangle: "))
b = float(input("Enter length of base of isosceles triangle: "))
height = math.sqrt(a**2 - (b**2 / 4))
area = (b * height) / 2
print("Area of Isosceles Triangle: ", area)