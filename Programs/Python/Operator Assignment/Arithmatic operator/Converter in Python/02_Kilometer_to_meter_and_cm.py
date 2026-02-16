# 2. **Kilometers to Meters &amp; Centimeters**
# Input distance in km; display meters and centimeters.

# Input Distance in Kilometer
km= float(input("Enter distance in kilometer: "))

# Conversion
meter= km * 1000
centimeter= meter * 100

# Output
print("Distance in Meter: ", round(meter, 2),"m")
print("distance in Centimeter: ", round(centimeter, 2),"cm")