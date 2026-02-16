# 25. **Area of Triangle using Heron’s Formula**
# Input 3 sides and compute area.

import math

# input values
a= float(input("\nEnter first side (a): "))
b= float(input("Enter second side (b): "))
c= float(input("Enter third side (c): "))

# Evaluating Semi-Parameter
s= (a+b+c)/2

# Calculating Area Using Heron's Formula
area= math.sqrt(s*(s-a)*(s-b)*(s-c))

# Output
print("Area of Triangle: ", round(area, 2),"\n")