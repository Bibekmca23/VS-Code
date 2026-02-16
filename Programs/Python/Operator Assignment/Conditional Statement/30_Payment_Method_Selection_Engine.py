# 10. Payment Method Selection Engine

# Description
# System selects payment method based on amount and wallet balance.

# Conditions
# If wallet_balance ≥ amount → Wallet
# Else if amount ≤ 50000 → Card
# Else → Net Banking

# Input Format
# amount (int)
# wallet_balance (int)

# Output Format
# <Payment Method>
# Expected Test Case

# Input
# 20000
# 5000

# Output
# Card

amount = int(input())
wallet_balance = int(input())

# condition
if wallet_balance >= amount:
    print("Wallet")
elif amount <= 50000:
    print("Card")
else:
    print("Net Banking")