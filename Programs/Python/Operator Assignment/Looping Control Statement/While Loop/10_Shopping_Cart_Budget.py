# Assignment 10: Shopping Cart Budget

# Scenario:
# A person has a fixed budget. Each item costs ₹100. Display remaining budget after each purchase.

# Condition:
# Item cost fixed
# Use a single while loop

# Input Format:
# Enter shopping budget

# Output Format:
# Remaining budget: XXX
# Budget exhausted

# Sample Input:
# 300

# Sample Output:
# Remaining budget: 200
# Remaining budget: 100
# Remaining budget: 0
# Budget exhausted

# code_1 
budget = int(input("Enter Shopping budget: "))
budget -= 100

while budget >= 0:
    print(f'Remaining Budget: {budget}')
    budget -= 100
print("Budget Exhausted")