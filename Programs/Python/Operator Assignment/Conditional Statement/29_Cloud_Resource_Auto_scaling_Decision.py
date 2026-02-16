# 9. Cloud Resource Auto-Scaling Decision

# Description
# Cloud system decides scaling action based on CPU and traffic.

# Conditions
# If CPU > 80 and traffic > 10000 → Scale Up Immediately
# Else if CPU > 70 → Scale Up
# Else if CPU < 30 → Scale Down
# Else → No Scaling

# Input Format
# cpu_usage (int)
# traffic (int)

# Output Format
# <Scaling Action>
# Expected Test Case

# Input
# 85
# 12000

# Output
# Scale Up Immediately

cpu_usage = int(input())
traffic = int(input())

# condition
if cpu_usage > 80 and traffic > 10000:
    print("Scale Up Immediately")
elif cpu_usage > 70:
    print("Scale Up")
elif cpu_usage < 30:
    print("Scale Down")
else:
    print("No Scaling")