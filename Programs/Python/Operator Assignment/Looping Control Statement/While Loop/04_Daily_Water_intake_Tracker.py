# Assignment 4: Daily Water Intake Tracker

# Scenario:
# A person drinks 250 ml water every time. Track water intake until the daily 
# goal is completed.

# Condition:
# Water intake is constant
# Use one while loop

# Input Format:
# Enter daily water goal in ml

# Output Format:
# Water consumed: XXX ml
# Goal achieved

# Sample Input:
# 1000

# Sample Output:
# Water consumed: 250 ml
# Water consumed: 500 ml
# Water consumed: 750 ml
# Water consumed: 1000 ml
# Goal achieved


# --------------------- code_1 ---------------------
# water = int(input("Enter daily water goal in ml: "))
# increment = 0
# while water >= increment:
#     increment += 250
#     if water >= increment:
#         print(f'Water Consumed: {increment}ml')
#     else:
#         print("Goal Achieved")


# --------------------- code_2 ---------------------
# water = int(input("Enter daily water goal in ml: "))
# increment = 250
# while water >= increment:
#     print(f'Water Consumed: {increment}ml')
#     increment += 250
# print("Goal Achieved")


# --------------------- code_3 ---------------------
# water = int(input("\nEnter daily water goal in ml: "))
# increment = 0
# while water >= increment:
#     r_water = water-increment
#     increment += 250
#     if water >= increment:
#         print(f'Water Consumed: {increment}ml')
#     elif r_water > 0:
#         print(f'Reamining Water to Consumed {r_water}')
#         drink= input("Drink rest of water(Y/N): ")
#         if drink == "Y" or drink == "y":
#             print(f'{water}ml Drinking Goal Achived')
#         elif drink == "N" or drink == "n":
#             print("You refuse to drink remaining water, you Looooser!!")
#     else:
#         print(f'{water}ml Drinking Goal Achived')


# --------------------- code_4 ---------------------
water = int(input("\nEnter daily water goal in ml: "))
limit = int(input("Set your Water consume quantity: "))
increment = 0
while water >= increment:
    r_water = water-increment
    increment += limit
    if water >= increment:
        print(f'Water Consumed: {increment} ml')
    elif r_water > 0:
        print(f'\nReamining Water to Consumed {r_water}')
        drink= input("Drink rest of water(Y/N): ")
        if drink == "Y" or drink == "y":
            print(f'\n{water} ml Drinking Goal Achived\n')
        elif drink == "N" or drink == "n":
            print("\nYou refuse to drink remaining water, you fu*king Looooser!!\n")
    else:
        print(f'\n{water} ml Drinking Goal Achived\n')




