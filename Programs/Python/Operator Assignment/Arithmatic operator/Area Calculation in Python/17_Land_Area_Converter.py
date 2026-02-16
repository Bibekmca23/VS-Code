# 17. **Land Area Converter**
# Input land dimensions in meters; output area in sq.m, sq.ft, and acres.

# Input dimensions in meters
length = float(input("\nEnter length in meters: "))
width  = float(input("Enter width in meters: "))

# Area in square meters
area_m2 = length * width

# Convert to square feet (1 m² = 10.7639 ft²)
area_ft2 = area_m2 * 10.7639

# Convert to acres (1 acre = 4046.8564224 m²)
area_acres = area_m2 / 4046.8564224

# Output results
print("\nArea in square meters:", area_m2)
print("Area in square feet:", area_ft2)
print("Area in acres:", area_acres,"\n")