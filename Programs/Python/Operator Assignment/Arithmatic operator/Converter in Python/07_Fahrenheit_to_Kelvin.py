# 7. **Fahrenheit to Kelvin**
# Convert using formula K = (F − 32) × 5/9 + 273.15.

# Input Temperature in Fahrenheit
fahrenheit= float(input("\nEnter temperature in fahrenheit: "))

# Conversion
kelvin= (fahrenheit - 32) * (5/9) + 273.15

# Output
print("Temperature in Kelvin: ", round(kelvin, 2),"°K\n")