# Assignment 5: Website Login Attempts

# Scenario:
# A user has limited login attempts. Each wrong attempt reduces one 
# chance. Display remaining attempts.

# Condition:
# Max attempts = user input
# Use a single while loop

# Input Format:
# Enter number of login attempts

# Output Format:
# Attempts left: X
# Account locked

# Sample Input:
# 3

# Sample Output:
# Attempts left: 2
# Attempts left: 1
# Attempts left: 0
# Account locked


# --------------------- code_1 --------------------- 
Max_attempts = int(input("Enter Maximum Attempts: "))
Max_attempts -= 1
while Max_attempts >= 0:
    print(f'Attempts Left: {Max_attempts}')
    Max_attempts -= 1
print("Account Locked")