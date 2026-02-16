# 6. Online Exam Result Processing
# Description
# Exam results are categorized using marks.

# Conditions
# ≥ 90 → Distinction
# ≥ 75 → First Class
# ≥ 60 → Second Class
# ≥ 40 → Pass
# Else → Fail

# Input Format
# marks (int)

# Output Format
# <Result>

# Expected Test Case

# Input
# 78

# Output
# First Class

# input
marks = int(input())

# condition
if marks >= 90:
    print("Distinction")
elif marks >= 75:
    print("First Class")
elif marks >= 60:
    print("Second Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")