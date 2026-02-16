# Assignment 8: Bus Ticket Counter

# Scenario:
# A bus has limited seats. One passenger boards at a time. Display remaining seats.

# Condition:
# One passenger per iteration
# Use only one while loop

# Input Format:
# Enter total seats

# Output Format:
# Seats remaining: X
# Bus full

# Sample Input:
# 2

# Sample Output:
# Seats remaining: 1
# Seats remaining: 0
# Bus full

# code_1
seats = int(input("Enter Total Seats: "))
seats -= 1
while seats >= 0:
    print(f'Seats Remaining: {seats}')
    seats -= 1
print("Bus Full")