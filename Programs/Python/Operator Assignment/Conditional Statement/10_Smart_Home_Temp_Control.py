# 10. Smart Home Temperature Control
# Description
# Controls appliances based on temperature.

# Conditions
# 30 → AC
# 20–30 → Normal
# < 20 → Heater

# Input Format
# temperature (float)

# Output Format
# <Action>

# Expected Test Case

# Input
# 18

# Output
# Turn ON Heater

# code
temperature = float(input())

# condition
if temperature >= 30:
    print("Turn AC ON")
elif temperature >= 20 and temperature < 30:
    print("Normal")
elif temperature < 20:
    print("Turn ON Heater")