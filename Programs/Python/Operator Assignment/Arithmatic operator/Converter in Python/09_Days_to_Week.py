# 9. **Days to Weeks and Days**
# Input number of days; convert to weeks + extra days.

# Input total days
days = int(input("\nEnter number of days: "))

# Conversion
# integer division
weeks = days // 7 
# remainder         
extra_days = days % 7      

# Output
print(weeks,"Weeks", extra_days,"Extra days\n")