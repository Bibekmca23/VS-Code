# 3. **Minutes to Hours**
# Input total minutes; convert into hours and remaining minutes.

# Input Total Minutes
minute= int(input("\nEnter total minutes: "))

# Minues to Hours
hour= minute // 60
remaining_minutes= minute % 60

# Output
print(hour,"Hour", remaining_minutes,"Minutes\n")