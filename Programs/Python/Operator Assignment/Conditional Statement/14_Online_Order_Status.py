# 14. Online Order Status System
# Description
# Displays order status using code.

# Conditions
# P → Processing
# S → Shipped
# D → Delivered
# C → Cancelled

# Input Format
# status_code (char)

# Output Format
# <Order Status>

# Expected Test Case
# Input
# D

# Output
# Delivered

# code 
print("""*** HERE ARE THE CODE TO ENTER ***
      P = Processing
      S = shipped
      D = Delivered
      C = Cancelled""")

status_code = (input())

# condition 
if status_code == "P" or status_code == "p":
    print("Processing")
elif status_code == "S" or status_code == "s":
    print("Shipped")
elif status_code == "D" or status_code == "d":
    print("Delivered")
elif status_code == "C" or status_code == "c":
    print("Cancelled")
else:
    print("*** ENTER THE RIGHT CODE ***")