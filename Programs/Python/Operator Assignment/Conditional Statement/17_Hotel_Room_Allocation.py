# 17. Hotel Room Allocation

# Description
# Allocates room if all conditions are satisfied.

# Conditions
# ID proof AND payment AND room availability → Allocated
# Else → Not Allocated

# Input Format
# id_proof (bool)
# payment_done (bool)
# room_available (bool)

# Output Format
# <Allocation Status>

# Expected Test Case
# Input
# True
# True
# False

# Output
# Room Not Allocated

# input code 
id_proof = input()
payment_done = input()
room_available = input()

# condition 
if (id_proof == "True" or id_proof == "true") and (payment_done == "True" or payment_done == "true") and (room_available == "True" or room_available == "true"):
    print("Room Allocated")
else:
    print("Room not Allocated")