# 2. Student Attendance Eligibility
# Description
# Exam eligibility based on attendance.

# Conditions
# ≥ 75 → Eligible
# 60–74 → Medical Review
# < 60 → Not Eligible

# Input Format
# attendance (int)

# Output Format
# <Status>

# Expected Test Case
# Input
# 65

# Output
# Medical Review Required

# code 
attendance = int(input())

# condition 
if attendance >= 75:
    print("Eligible")
elif attendance >= 60 and attendance < 75:
    print("Medical Review Required")
else:
    print("Not Eligible")