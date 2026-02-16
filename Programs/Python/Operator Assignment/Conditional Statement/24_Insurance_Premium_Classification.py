# 4. Insurance Premium Classification

# Description
# Insurance premium category depends on age, health score, and smoking 
# status.

# Conditions
# If smoker and health_score < 50 → High Premium
# Else if age > 45 and health_score < 60 → High Premium
# Else if health_score < 75 → Medium Premium
# Else → Low Premium

# Input Format
# age (int)
# health_score (int)
# is_smoker (bool)

# Output Format
# <Premium Category>

# Expected Test Case
# Input
# 50
# 55
# False

# Output
# High Premium

age = int(input())
health_score = int(input())
is_smoker = input()

if is_smoker == "True" or is_smoker == "true" and health_score < 50:
    print("High Premium")
elif age > 45 and health_score < 60:
    print("Health Premium")
elif health_score < 75:
    print("Medium Premium")
else:
    print("Low Premium")