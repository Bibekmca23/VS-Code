# 11. Cab Fare Estimator
# Description
# Calculates fare using distance slabs.

# Conditions
# ≤ 5 km → ₹50
# 6–15 km → ₹10/km
# 15 km → ₹8/km

# Input Format
# distance (float)

# Output Format
# Total Fare: <amount>

# Expected Test Case

# Input
# 12

# Output
# Total Fare: 120

distance = float(input())

if distance <= 5:
    print(f'Total Fare: {distance * 50}₹')
elif distance >= 6 and distance < 15:
    print(f'Total Fare: {distance * 10}₹')
else:
    print(f'Total Fare: {distance * 8}₹')