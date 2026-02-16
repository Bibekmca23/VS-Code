# 18. Online Shopping Return Policy

# Description
# Validates product return eligibility.

# Conditions
# ≤ 7 days AND unused AND bill available → Accepted
# Else → Rejected

# Input Format
# days_since_purchase (int)
# unused (bool)
# bill_available (bool)

# Output Format
# <Return Status>

# Expected Test Case
# Input
# 5
# True
# True

# Output
# Return Accepted

# input code 
days_since_purchase = int(input("Enter days since purchase: "))

if days_since_purchase <= 7:
    unused = input("Is the product unused? (True/False): ")
    if unused == "True" or unused == "true" :
        bill_available = input("Is the bill available? (True/False): ") 
        if bill_available == "True" or bill_available == "true":
            print("Return Accepted")
        else:
            print("Product Return Rejected")
    else:
        print("Product Return Rejected")
else:
    print("Product Return Date Alredy Passed")