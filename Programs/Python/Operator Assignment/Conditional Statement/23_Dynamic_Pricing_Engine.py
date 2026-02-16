# 3. Dynamic Pricing Engine

# Description
# An e-commerce platform calculates final price using demand and customer 
# type.

# Conditions
# If demand = "High" and customer = "VIP" → 30% markup
# If demand = "High" → 20% markup
# If demand = "Medium" → 10% markup
# Else → No markup

# Input Format
# base_price (float)
# demand (str)
# customer_type (str)

# Output Format
# Final Price: <amount>

# Expected Test Case
# Input
# 1000
# High
# VIP

# Output
# Final Price: 1300

base_price = float(input())
demand = input()
customer_type = input()

if demand == "High" or demand == "high" and customer_type == "VIP" or customer_type == "vip":
    percentage = base_price * (3/10)
    print(f'Final Price: {base_price + percentage}')
elif demand == "High" or demand == "high":
    percentage = base_price * (2/10)
    print(f'Final Price: {base_price + percentage}')
elif demand == "Medium" or demand == "medium":
    percentage = base_price * (1/10)
    print(f'Final Price: {base_price + percentage}')
else:
    print("No Markup")