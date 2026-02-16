# . Traffic Signal Controller
# Description
# Displays traffic action based on signal color.

# Conditions
# Red → Stop
# Yellow → Ready
# Green → Go
# Otherwise → Invalid Signal

# Input Format
# signal (str)

# Output Format
# <Action>

# Expected Test Case

# Input
# Green

# Output
# Go

# input
signal = input()

# Condition
if signal == "Red" or signal == "red" or signal == "RED":
    print("Stop")
elif signal == "Yellow" or signal == "yellow" or signal == "YELLOW":
    print("Ready")
elif signal == "Green" or signal == "green" or signal == "GREEN":
    print("Go")
else:
    print("Invalid Signal")