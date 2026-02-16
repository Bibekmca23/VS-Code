# Assignment 2: Product Budget Check
# Use Case: Online shopping
# Input:
# price = 850
# budget = 1000
# Output:
# True

price= float(input("\nEnter price of product: "))
budget= float(input("Enter your budget: "))

if price<=budget:
    print("True\n")
else:
    print("Over Price\n")