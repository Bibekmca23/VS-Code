# Assignment 2: ATM Cash Withdrawal

# Scenario:
# An ATM machine has a certain amount of cash. Each customer withdraws 
# ₹500. Display remaining cash after each withdrawal until ATM is empty.

# Condition:
# Withdrawal amount is fixed (₹500)
# Use a single while loop

# Input Format:
# Enter total cash in ATM

# Output Format:
# Remaining cash: XXXX
# ATM empty

# Sample Input:
# 2000

# Sample Output:
# Remaining cash: 1500
# Remaining cash: 1000
# Remaining cash: 500
# Remaining cash: 0
# ATM empty

# ------------------ code_1 ------------------ 
# atm = int(input("Enter total cash in ATM: "))

# while atm >= 0:
#     atm -= 500
#     if atm >= 0:
#         print(f'Remaining Cash: {atm}₹')
#     else:
#         print("ATM Empty")


# ------------------ code_2 ------------------ 
# atm = int(input("Enter total cash in ATM: "))

# while atm >= 0:
#     atm -= 500
#     if atm >= 0:
#         print(f'Remaining Cash: {atm}₹')
# print("ATM Empty")


# ------------------ code_3 ------------------ 
# atm = int(input("Enter total cash in ATM: "))

# while atm >= 0:
#     print(f'Remaining Cash: {atm}₹')
#     atm -= 500
# print("ATM Empty")