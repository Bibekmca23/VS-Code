# Assignment 3: Online Class Attendance

# Scenario:
# An online class starts with 0 students. Students join one by one. Display 
# total students until class limit is reached.

# Condition:
# Students join one at a time
# Use a single while loop

# Input Format:
# Enter maximum class strength

# Output Format:
# Student joined: 1
# Student joined: 2
# ...
# Class full

# Sample Input:
# 3

# Sample Output:
# Student joined: 1
# Student joined: 2
# Student joined: 3
# Class full

# ------------------------ code_1 ------------------------
# max_student = int(input("Enter Maximum Class Strength: "))
# i = 0

# while max_student >= i:
#     i += 1
#     if i<= max_student:
#         print(f'Student Joined: {i}')
#     else:
#         print("Class Full")



# ------------------------ code_2 ------------------------
# max_student = int(input("Enter Maximum Class Strength: "))
# i = 1

# while max_student >= i:
#     print(f'Student Joined: {i}')
#     i += 1

# print("Class Full")