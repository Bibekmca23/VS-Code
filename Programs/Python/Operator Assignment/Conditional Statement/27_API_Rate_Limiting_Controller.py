# 7. API Rate Limiting Controller

# Description
# API access is limited based on user tier and request count.

# Conditions
# If requests > 1000 → Blocked
# Else if tier = "Free" and requests > 100 → Rate Limited
# Else if tier = "Pro" and requests > 500 → Rate Limited
# Else → Access Granted

# Input Format
# tier (str)
# requests (int)

# Output Format
# <API Status>
# Expected Test Case

# Input
# Free
# 150

# Output
# Rate Limited

tier = input()
requests = int(input())

# condition
if requests > 1000:
    print("Blocked")
elif tier == "Free" or tier == "free" and requests > 100:
    print("Rate Limited")
elif tier == "Pro" or tier == "pro" and requests > 500:
    print("Rate limited")
else:
    print("Access Granted")