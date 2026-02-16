# 23. **Area of Oval (Ellipse)**
# Input two radii a and b; area = πab.

import math

# input radii values
a= float(input("\nEnter semi-major radii (a): "))
b= float(input("Enter semi-minor radii (b): "))

# Calculating Area of Ellipse
area= math.pi * a * b

# output
print("Area of Oval(Ellipse): ", round(area, 2),"\n")