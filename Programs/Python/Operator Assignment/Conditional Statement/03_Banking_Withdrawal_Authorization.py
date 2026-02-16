# 3. Banking Withdrawal Authorization
# Description
# Withdrawal is permitted only when account conditions are satisfied.

# Conditions
# If account inactive → Account Inactive
# If withdraw amount > daily limit → Daily Limit Exceeded
# If withdraw amount > balance → Insufficient Balance
# Else → Withdrawal Successful

# Input Format
# account_active (bool)
# balance (float)
# withdraw_amount (float)
# daily_limit (float)

# Output Format
# <Withdrawal Status>

# Expected Test Case

# Input
# True
# 5000
# 3000
# 4000

# Output
# Withdrawal Successful

# input
account_active= input()

# Condition
if account_active == "True" or account_active == "true":    
    balance= float(input())
    withdraw_amount= float(input())
    daily_limit= float(input())
    if withdraw_amount > daily_limit:
        print("Daily Limit Exceeded")
    elif withdraw_amount > balance:
        print("Insufficient Balance")
    else:
        print("Withdrawal Successful")
else:
    print("Account Inactive")








# code_2
# account_active= input("User Active (True/False): ")

# # Condition
# if account_active == "True" or account_active == "true":    
#     balance= float(input())
#     withdraw_amount= float(input())
#     daily_limit= float(input())
#     if withdraw_amount > daily_limit:
#         print("Daily Limit Exceeded")
#     elif withdraw_amount > balance:
#         print("Insufficient Balance")
#     else:
#         print("Withdrawal Successful")
# else:
#     print("Account Inactive")