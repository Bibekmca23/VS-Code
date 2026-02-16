# 7. Loan Approval System
# Description
# Loan approval depends on age, salary, and credit score.

# Conditions
# Age < 21 → Reject (Age)
# Salary < 25000 → Reject (Salary)
# Credit score < 650 → Reject (Credit)
# Else → Approved

# Input Format
# age (int)
# salary (int)
# credit_score (int)

# Output Format
# Loan Approved / Loan Rejected: <Reason>

# Expected Test Case

# Input
# 25
# 30000
# 700

# Output
# Loan Approved

# input with condition
age = int(input())
if age > 21:
    salary = int(input())
    if salary > 25000:
        credit_score = int(input())
        if credit_score > 650:
            print("Loan Approved")
        else:
            print(f'Loan Rejected: Your Credit score below {credit_score}')
    else:
        print(f'Loan Rejected: Your Salary Below {salary}')
else:
    print(f'Loan Rejected: Your Age is Below {age}')