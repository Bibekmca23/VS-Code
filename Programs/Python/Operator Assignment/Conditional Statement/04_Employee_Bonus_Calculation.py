# 4. Employee Bonus Calculation
# Description
# Company calculates bonus based on experience and rating.

# Conditions
# Experience ≥ 5 and rating ≥ 4 → 20%
# Experience ≥ 3 → 15%
# Experience ≥ 1 → 10%
# Else → 0%

# Input Format
# experience (int)
# rating (int)

# Output Format
# Bonus: <percentage>%

# Expected Test Case

# Input
# 4
# 3

# Output
# Bonus: 15%

# Input
experience = int(input())
rating = int(input())

# Condition
if experience >= 5:
    if rating >= 4 and rating <= 10:
        print("Bonus: 20%")
    else:
        print("Enter Rating Between 1 to 10")
elif experience >= 3:
    print("Bonus: 15%")
elif experience >= 1:
    print("Bonus: 10%")
else:
    print("Bonus: 0%")