# 1. User Login Access Validation
# Description
# A login system validates a user based on account status, login attempts, 
# and password correctness.

# Conditions
#  If user is not active → User Inactive
#  Else if attempts ≥ 3 → Account Locked
#  Else if password is incorrect → Invalid Password
#  Else → Login Successful

# Input Format
# is_active (bool)
# password_correct (bool)
# attempts (int)

# Output Format
# <Login Status Message>

# Expected Test Case
# Input
# True
# True
# 1

# Output
# Login Successful

# Input
is_active = input("User is active (True/False): ")
password_correct = input("Password input (True/False): ")
attempts = int(input("User attempts time: "))

# Conditions
if is_active == "True" or is_active == "true":
    if password_correct == "True" or password_correct == "true":
        if attempts >= 3:
            print("Account Locked")
        else:
            print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("User Inactive")