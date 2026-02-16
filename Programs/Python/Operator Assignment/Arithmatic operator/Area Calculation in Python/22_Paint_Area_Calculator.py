# 22. **Paint Area Calculator**
# Calculate wall area excluding windows and doors.

wall_len= float(input("\nEnter Length of wall: "))
wall_wid= float(input("Enter Width of wall: "))

door_len= float(input("Enter length of door:"))
door_wid= float(input("Enter width of door:"))

window_height= float(input("Enter window height: "))
window_width= float(input("Enter window width: "))

wall_area= wall_len * wall_wid

door_area= door_len * door_wid
window_area= window_height * window_width

Total_area= wall_area - (door_area + window_area)

print("Area of Wall: ", wall_area,"meter")
print("Area of Door: ", door_area,"meter")
print("Area of Window: ", window_area,"meter")
print("Total Wall Area to paint: ", Total_area,"meter\n")