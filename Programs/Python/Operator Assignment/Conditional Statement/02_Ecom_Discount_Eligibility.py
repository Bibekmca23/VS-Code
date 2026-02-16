# 2. E-Commerce Discount Eligibility

# Description
# An online store provides discounts based on purchase amount and 
# membership type.

# Conditions
# Amount ≥ 10000 and premium → 30%
# Amount ≥ 10000 → 20%
# Amount ≥ 5000 → 10%
# Otherwise → 0%

# Input Format
# amount (int)
# is_premium (bool)

# Output Format
# Discount: <percentage>%
# Expected Test Case

# Input
# 12000
# False

# Output
# Discount: 20%

# Input
amount = int(input())
is_premium = input()

# Conditions
if amount >= 10000:
    if is_premium == "true" or is_premium == "True":
        print("Discount: 30%")
    else:
        print("Discount: 20%")
elif amount >= 5000 and amount <= 10000:
        print("Discount: 10%")
else:
    print("Discount: 0%")