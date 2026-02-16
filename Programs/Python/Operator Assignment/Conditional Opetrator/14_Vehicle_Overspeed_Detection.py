# Assignment 14: Vehicle Overspeed Detection
# Use Case: Traffic monitoring
# Input:
# speed = 95
# Condition:
# Speed ≤ 80
# Output:
# False

speed= int(input("\nEnter vehicle speed: "))

if speed <= 80:
    print("True\n")
else:
    print("False\n")