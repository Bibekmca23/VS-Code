# 13. Server Load Monitoring
# Description
# Monitors server load.

# Conditions
# < 50 → Low
# 50–80 → Medium
# 80 → High Alert

# Input Format
# load_percentage (int)

# Output Format
# <Load Status>

# Expected Test Case
# Input
# 85

# Output
# High Load Alert

load_percentage = int(input())

if load_percentage < 50:
    print("Server Load: Low")
elif load_percentage >= 50 and load_percentage < 80:
    print("Server Load: Medium")
else:
    print("High Load Alert")