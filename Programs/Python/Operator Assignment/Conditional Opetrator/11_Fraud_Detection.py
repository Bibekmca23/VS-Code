# Assignment 11: Fraud Detection
# Use Case: Banking system
# Input:
# entered_amount = 10000
# actual_amount = 10050
# Condition:
# Entered amount == Actual amount
# Output:
# False

entered_amount= float(input("\nEnter your amount: "))
actual_amount= 10050

if entered_amount==actual_amount:
    print("True\n")
else:
    print("False\n")