# Assignment 9: Cloud Storage Limit
# Use Case: Cloud services
# Input:
# used_storage = 55
# limit = 50
# Condition:
# Used storage ≤ Limit
# Output:
# False

used_storage= int(input("\nEnter used storage: "))
limit= int(input("Enter limit of storage: "))

if used_storage<=limit:
    print("True\n")
else:
    print("False\n")