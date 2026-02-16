# 13. **Calculate Cost Based on Area**
# A painter charges ₹10 per sq.ft; find total cost for a rectangular wall.

length = float(input("Enter length of wall (in ft): "))
breadth = float(input("Enter breadth of wall (in ft): "))

area = length * breadth
cost_per_sqft = 10
total_cost = area * cost_per_sqft
print("Total cost to paint the wall", total_cost)