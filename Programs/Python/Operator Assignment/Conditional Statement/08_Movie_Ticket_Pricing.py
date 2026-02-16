# 8. Movie Ticket Pricing
# Description
# Ticket price varies by age and weekend.

# Conditions
# Age < 12 → ₹100
# Age 12–60 → ₹200
# Age > 60 → ₹150
# Weekend → +₹50

# Input Format
# age (int)
# is_weekend (bool)

# Output Format
# Ticket Price: <amount>

# Expected Test Case

# Input
# 30
# True

# Output
# Ticket Price: 250

# code
age = int(input())
is_weekend = input()

if age < 12:
    if is_weekend == "True" or is_weekend == "true" or is_weekend == "TRUE":
        print(f'Ticket Price: {100+50}')
    else:
        print(f'Ticket Price: 100')
elif age >= 12 and age < 60:
    if is_weekend == "True" or is_weekend == "true" or is_weekend == "TRUE":
        print(f'Ticket Price: {200+50}')
    else:
        print(f'Ticket Price: 200')
elif age >= 60:
    if is_weekend == "True" or is_weekend == "true" or is_weekend == "TRUE":
        print(f'Ticket Price: {150+50}')
    else:
        print(f'Ticket Price: 150')