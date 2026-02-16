# 16. Mobile Recharge Validity Checker

# Description
# Shows validity based on plan type.

# Conditions
# Daily → 1 day
# Weekly → 7 days
# Monthly → 30 days

# Input Format
# plan_type (str)

# Output Format
# Validity: <days> days

# Expected Test Case
# Input
# Monthly

# Output
# Validity: 30 days

print("""*** ENTER DAY AS INPUT ***
      Daily,
      Weekly,
      Monthly""")
plan_type = input()

if plan_type == "Daily" or plan_type == "daily":
    print(f'Validity: 1 days')
elif plan_type == "Weekly" or plan_type == "weekly":
    print(f'Validity: 7 days')
elif plan_type == "Monthly" or plan_type == "monthly":
    print(f'Validity: 30 days')