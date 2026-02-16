# 2. Credit Card Transaction Risk Assessment

# Description
# A bank evaluates transaction risk before approval.

# Conditions
# If transaction_amount > 100000 → High Risk
# Else if international_transaction and amount > 50000 → High Risk
# Else if failed_attempts ≥ 3 → Transaction Blocked
# Else → Transaction Approved

# Input Format
# transaction_amount (float)
# international_transaction (bool)
# failed_attempts (int)

# Output Format
# <Transaction Status>

# Expected Test Case
# Input
# 60000
# True
# 1

# Output
# High Risk

transaction_amount = float(input())
international_transaction = input()
failed_attempts = int(input())

if transaction_amount > 100000:
    print("High Risk")
elif international_transaction == "True" or international_transaction == "true" and transaction_amount > 50000:
    print("High Risk")
elif failed_attempts >= 3:
    print("Transaction Blocked")
else:
    print("Transaction Approved")