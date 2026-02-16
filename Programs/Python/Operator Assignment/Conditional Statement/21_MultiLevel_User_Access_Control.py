# Conditional Statements Exam-21. Multi-Level User Access Control

# Description
# A system grants access based on role, account status, and security 
# clearance.

# Conditions
# If account inactive → Access Denied: Inactive Account
# Else if role = "Admin" and clearance ≥ 5 → Full Access
# Else if role = "Manager" and clearance ≥ 3 → Manager Access
# Else if role = "Employee" → Limited Access
# Else → Access Denied

# Input Format
# role (str)
# is_active (bool)
# clearance (int)

# Output Format
# <Access Level>

# Expected Test Case
# Input
# Admin
# True
# 6

# Output
# Full Access

# input code 
role = input()
is_active = input()
clearance = int(input())

# condition 
if is_active == "True" or is_active == "true":
    if role == "Admin" or role == "admin" and clearance >= 5:
        print("Full Access")
    elif role == "Manager" or role == "manager" and clearance >= 3:
        print("Manager Access")
    elif role == "Employee" or role == "employee":
        print("Limited Access")
    else:
        print("Access Denied")
else:
    print("Access Denied: Inactive Account")