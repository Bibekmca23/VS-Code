# Assignment 1: Mobile Battery Drain

# Scenario:
# A mobile phone battery starts at a given percentage. Every hour, the 
# battery drains by 5%. Display the battery level hour by hour until it reaches 
# 0 or below.

# Condition:
# Use only one while loop
# Battery reduces by 5 each iteration

# Input Format:
# Enter initial battery percentage

# Output Format:
# Battery after 1 hour: 95%
# Battery after 2 hours: 90%
# ...
# Battery drained

# Sample Input:
# 20

# Sample Output:
# Battery after 1 hour: 15%
# Battery after 2 hours: 10%
# Battery after 3 hours: 5%
# Battery after 4 hours: 0%
# Battery drained

# ------------------------ code_1 ------------------------ 
# battery = int(input("Enter Initial Battery Percentage: "))
# t = 0
# while battery >= 0:
#     battery -= 5
#     t += 1
#     if battery >= 0:
#         print(f'Battery After {t} hour: {battery}%')
#     else:
#         print("Battery drained")



# ------------------------ code_2 ------------------------ 
battery = int(input("Enter Initial Battery Percentage: "))
battery -= 5
t = 1
while battery >= 0:
    print(f'Battery After {t} hour: {battery}%')
    t += 1
    battery -= 5
print("Battery drained")