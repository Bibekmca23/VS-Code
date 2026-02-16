# 11. Customer Support Ticket Priority

# Description
# Support tickets are prioritized dynamically.

# Conditions
# If customer_type = "Enterprise" and issue_severity = "Critical" → P1
# Else if issue_severity = "Critical" → P2
# Else if issue_severity = "High" → P3
# Else → P4

# Input Format
# customer_type (str)
# issue_severity (str)

# Output Format
# <Ticket Priority>

# Expected Test Case
# Input
# Enterprise
# Critical

# Output
# P1

customer_type = input()
issue_severity = input()

# condtion
if customer_type == "enterprise" or customer_type == "Enterprise" and issue_severity == "critical" or issue_severity == "Critical":
    print("P1")
elif issue_severity == "critical" or issue_severity == "Critical":
    print("P2")
elif issue_severity == "High":
    print("P3")
else:
    print("P4")