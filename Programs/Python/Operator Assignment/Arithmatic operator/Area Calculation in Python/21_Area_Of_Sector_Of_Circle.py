# 21. **Area of Sector of a Circle**
# Input radius and angle (in degrees or radians).

import math

radius= float(input("\nEnter radius of circle: "))
degree= float(input("Enter angle in degree: "))

# Area using degree formula
area= (degree/360) * math.pi * (radius**2)

# print("Area of Sector: ",round(area, 2),"°\n")
print(f'Area of Sector: {round(area, 2)}°')