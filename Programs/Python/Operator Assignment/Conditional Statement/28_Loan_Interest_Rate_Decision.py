# 8. Loan Interest Rate Decision

# Description
# Bank assigns interest rate category based on profile.

# Conditions
# If credit_score ≥ 750 and salary ≥ 80000 → Low Interest
# Else if credit_score ≥ 650 → Medium Interest
# Else → High Interest

# Input Format
# credit_score (int)
# salary (int)

# Output Format
# <Interest Category>
# Expected Test Case

# Input
# 720
# 60000

# Output
# Medium Interest

credit_score = int(input())
salary = int(input())

# condition
if credit_score >= 750 and salary >= 80000:
    print("Low interest")
elif credit_score >= 650:
    print("Medium interest")
else:
    print("High interest")