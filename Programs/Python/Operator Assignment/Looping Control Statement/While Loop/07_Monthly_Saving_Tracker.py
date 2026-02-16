# Assignment 7: Monthly Savings Tracker

# Scenario:
# A person saves ₹2000 every month. Track savings until the target amount 
# is reached.

# Condition:
# Monthly saving is fixed
# Single while loop

# Input Format:
# Enter savings target

# Output Format:
# Total savings: XXXX
# Target achieved

# Sample Input:
# 6000

# Sample Output:
# Total savings: 2000
# Total savings: 4000
# Total savings: 6000
# Target achieved

# --------------------- code_1 --------------------- 
# target = int(input("Enter saving target: "))
# saving = 2000
# while saving <= target:
#     print(f'Total Saving: {saving}')
#     saving += 2000
# print("Target Achived")


# --------------------- code_2 ---------------------
# s_target = int(input("\nEnter saving target amount: "))
# m_target = int(input("Enter monthly saving amount: "))
# saving = m_target
# m = 1
# while saving <= s_target:
#     print(f'{m} Month Saving: {saving}')
#     saving += m_target
#     m += 1
# print("Your Saving Money Target Achived\n")