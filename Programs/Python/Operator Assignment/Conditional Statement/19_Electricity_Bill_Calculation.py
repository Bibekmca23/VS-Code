# 19. Electricity Bill Calculation

# Description
# Calculates bill using slab rates.

# Conditions
# ≤ 100 → ₹2/unit
# ≤ 300 → ₹3/unit
# 300 → ₹5/unit

# Input Format
# units (int)

# Output Format
# Total Bill: <amount>

# Expected Test Case
# Input
# 350

# Output
# Total Bill: 1450

units = int(input())

if units <= 100:
    first = units * 2
    print(f'Total Bill: {first}₹')
elif units <= 300:
    first = 100 * 2
    a = ( units - 100) * 3
    second = first + a
    print(f'Total Bill: {second}₹')
else:
    first = 100 * 2
    a = 200 * 3
    second = first + a
    b = (units - 300) * 5
    third = second + b
    print(f'Total Bill: {third}₹')
