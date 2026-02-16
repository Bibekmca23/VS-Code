# 14. **Garden Plot Area**
# A rectangular garden has a circular fountain cut out in the center. Find the remaining area.

import math

# Input dimensions
length = float(input("Enter garden length (m): "))
width  = float(input("Enter garden width (m): "))
radius = float(input("Enter fountain radius (m): "))

# Areas
rect_area = length * width
circle_area = math.pi * (radius ** 2)

# Remaining area
remaining_area = rect_area - circle_area

# Output
print("Garden area (rectangle):", rect_area)
print("Fountain area (circle):", circle_area)
print("Remaining area:", remaining_area)


# Upgrade version *** 

# import math

# length = float(input("Enter length of the rectangular garden: "))
# width = float(input("Enter width of the rectangular garden: "))
# radius = float(input("Enter radius of the circular fountain: "))

# rect_area = length * width
# circle_area = math.pi * radius ** 2
# remaining_area = rect_area - circle_area

# if remaining_area < 0:
#     print("Error: Fountain area is larger than the garden!")
# else:
#     print("Remaining Garden Area", remaining_area)