# 15. **Room Flooring Calculator**
# Given room dimensions and tile area, find number of tiles needed.

import math

# Input room dimensions
room_length = float(input("\nEnter length of the room: "))
room_width = float(input("Enter width of the room: "))

# Input tile dimensions
tile_length = float(input("Enter length of a tile: "))
tile_width = float(input("Enter width of a tile: "))

# Calculate areas
room_area = room_length * room_width
tile_area = tile_length * tile_width

# Calculate number of tiles (rounded up)
tiles_needed = math.ceil(room_area / tile_area)

print("\nRoom Area: ", room_area,"Sq Units")
print("Tile Area: ", tile_area,"Sq Units")
print("Number of Tiles Needed: ", tiles_needed,"\n")