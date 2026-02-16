# 20. Company Promotion Eligibility

# Description
# Checks promotion eligibility.

# Conditions
# Experience ≥ 3 AND rating ≥ 4 AND no disciplinary action → 
# Approved
# Else → Denied

# Input Format
# experience (int)
# rating (int)
# disciplinary_action (bool)

# Output Format
# <Promotion Status>

# Expected Test Case
# Input
# 5
# 4
# False

# Output
# Promotion Approved

experience = int(input())
rating = int(input())
disciplinary_action = input()

if experience >= 3 and rating >= 4 and disciplinary_action == "False" or disciplinary_action == "false":
    print("Promotion Approved")
else:
    print("Promotion Rejected")