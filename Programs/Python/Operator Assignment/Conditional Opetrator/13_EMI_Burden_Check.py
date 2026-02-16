# Assignment 13: EMI Burden Check
# Use Case: Loan system
# Input:
# emi = 18000
# income = 15000
# Condition:
# EMI ≤ Income
# Output:
# False

emi= int(input("\nEnter EMI amount: "))
income= int(input("Enter your income: "))

if emi<=income:
    print("True\n")
else:
    print("False\n")