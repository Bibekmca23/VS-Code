# 🟥 CHALLENGE SET 1 — EXTREME RESTRICTIONS
# 1️⃣ Number Classification Engine

# **Input:** One integer `n`

# **Output (only ONE):**
# * `"Positive Even"`
# * `"Positive Odd"`
# * `"Negative Even"`
# * `"Negative Odd"`
# * `"Zero"`

# ❌ Restrictions:
# ❌ No nested `if`
# ❌ No logical operators (`and`, `or`, `not`)
# ❌ No modulo operator `%`
# 💡 *Interview focus:* Mathematical thinking without `%`.
# ✔️ Only comparison operators and arithmetic
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

num=int(input("enter a number: "))

a=num/2
b=int(a)
if num>0:
    sign="Positive"
if num<0:
    sign="Negative"
if num==0:
    print("zero")
if a==b:
    p="Even"
else:
    p="Odd"
print(sign+" "+p)


# num=int(input())
# r=num-2*(num//2)
# if num>0:
#     sign="Positive"
# if num<0:
#     sign="Negative"
# if r==0:
#     a="Even"
# if r==1:
#     a="Odd"
# else:
#     print("Zero")

# print(sign+" "+a)


# n = int(input("Enter a number: "))
# if (n > 0) * ((n // 2) * 2 == n):
#     print("Positive Even")
# elif (n > 0) * ((n // 2) * 2 != n):
#     print("Positive Odd")
# elif (n < 0) * ((n // 2) * 2 == n):
#     print("Negative Even")
# elif (n < 0) * ((n // 2) * 2 != n):
#     print("Negative Odd")
# else:
#     print("Zero")















































# water = int(input("\nEnter daily water goal in ml: "))
# limit = int(input("Set your Water consume quantity: "))
# increment = 0
# while water >= increment:
#     r_water = water-increment
#     increment += limit
#     if water >= increment:
#         print(f'Water Consumed: {increment} ml')
#     elif r_water > 0:
#         print(f'\nReamining Water to Consumed {r_water}')
#         drink= input("Drink rest of water(Y/N): ")
#         if drink == "Y" or drink == "y":
#             print(f'\n{water} ml Drinking Goal Achived\n')
#         elif drink == "N" or drink == "n":
#             print("\nYou refuse to drink remaining water, you fu*king Looooser!!\n")
#     else:
#         print(f'\n{water} ml Drinking Goal Achived\n')

































































































































































































