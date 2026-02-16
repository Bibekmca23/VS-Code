# 6. Employee Performance Action System

# Description
# HR decides action based on rating and warnings.

# Conditions
# If rating < 2 and warnings ≥ 2 → Termination
# Else if rating < 3 → Performance Improvement Plan
# Else if rating ≥ 4 and warnings = 0 → Promotion Consideration
# Else → No Action

# Input Format
# rating (float)
# warnings (int)

# Output Format
# <Action>
# Expected Test Case

# Input
# 4.5
# 0

# Output
# Promotion Consideration

rating = float(input())
warnings = int(input())

# condition 
if rating < 2 and warnings >= 2:
    print("Termination")
elif rating < 3:
    print("Performance Improvemnet Plan")
elif rating >= 4 and warnings == 0:
    print("Promotion Consideration")
else:
    print("No Action")