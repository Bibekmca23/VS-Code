# 15. Salary Tax Slab Calculation

# Description
# Determines tax rate based on salary.

# Conditions
# ≤ 3L → 0%
# ≤ 6L → 5%
# ≤ 10L → 10%
# 10L → 20%

# Input Format
# annual_salary (int)

# Output Format
# Tax Rate: <percentage>%

# Expected Test Case
# Input
# 750000

# Output
# Tax Rate: 10%

annual_salary = int(input())

if annual_salary <= 300000:
    print("Tax Rate: 0%")
elif annual_salary > 300000 and annual_salary <= 600000:
    print("Tax Rate: 5%")
elif annual_salary > 600000 and annual_salary <= 1000000:
    print("Tax Rate: 10%")
else:
    print("Tax Rate: 20%")