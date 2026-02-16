# Assignment 6: Elevator Floor Counter

# Scenario:
# An elevator starts at ground floor (0) and goes up one floor at a time until it 
# reaches the destination floor.

# Condition:
# Move one floor per loop
# Use only one while loop

# Input Format:
# Enter destination floor

# Output Format:
# Current floor: X
# Reached destination

# Sample Input:
# 4

# Sample Output:
# Current floor: 1
# Current floor: 2
# Current floor: 3
# Current floor: 4
# Reached destination

# code_1 
floor = int(input("Enter destination floor: "))
destination = 1
while destination <= floor:
    print(f'Current Floor: {destination}')
    destination += 1
print("Reached destination")