# 5. Smart Inventory Reorder System

# Description
# Warehouse system decides reorder priority.

# Conditions
# If stock = 0 → Critical Reorder
# Else if stock < minimum and supplier_available → Immediate Reorder
# Else if stock < minimum → Reorder Pending
# Else → Stock Sufficient

# Input Format
# stock (int)
# minimum (int)
# supplier_available (bool)

# Output Format
# <Reorder Status>
# Expected Test Case

# Input
# 5
# 10
# True

# Output
# Immediate Reorder

stock = int(input())
minimum = int(input())
supplier_available = input()

# condition 
if stock == 0:
    print("Critical Reorder")
elif stock < minimum and supplier_available == "True" or supplier_available == "true":
    print("Immediate Reorder")
elif stock < minimum:
    print("Reorder Pending")
else:
    print("Stock Sufficient")