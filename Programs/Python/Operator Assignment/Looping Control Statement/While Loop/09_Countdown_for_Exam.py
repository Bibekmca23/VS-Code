# Assignment 9: Countdown for Exam

# Scenario:
# An exam starts in N seconds. Display countdown until exam begins.

# Condition:
# Countdown decreases by 1
# Single while loop

# Input Format:
# Enter countdown time

# Output Format:
# Time left: X
# Exam started

# Sample Input:
# 3

# Sample Output:
# Time left: 3
# Time left: 2
# Time left: 1
# Exam started

# code_1 
time = int(input("Enter countdown time: "))
while time >= 1:
    print(f'Time Left: {time}')
    time -= 1
print("...\nExam Started")