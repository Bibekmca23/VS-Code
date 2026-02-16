# a=1+2j
# b=3+2j
# print(a+b)

# c=2j
# d=1+4
# print(c+d)

# e=2
# f=1j
# print(e+f)

# g=True
# h=False
# print(g+h)

# i="Bibek"
# j="Muduli"
# print(i,j,i+j)

# k=True
# l=1+2j
# print(k+l)

# m=1+2j+1+2.5+True
# print(m)


# Write a program to input Student name, 2 subject marks
# calculate total marks

# s_name=input("Enter student name: ")
# mark_1=int(input("Enter first subject mark: "))
# mark_2=int(input("Enter second subject mark:"))

# t_mark=mark_1+mark_2
# print(f'Total Marks of {s_name} are {t_mark}')


# a=5+2j
# b=3+2j
# print(a-b)

# c=2j
# d=1-4
# print(c-d)

# e=2
# f=1j
# print(e-f)

# g=True
# h=False
# print(g-h)

# k=True
# l=1+2j
# print(k-l)

# m=1+2j-1-2.5-True
# print(m)


# Write a program to input 2 integer numbers and swap
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# print(f'numbers befor swap a={a} and b={b}')
# c=a
# a=b
# b=c
# print(f'after swap a={a} and b={b}')

# # Without using Third Variable
# a=a+b
# b=a-b
# a=a-b
# print(f'again swaping a={a} and b={b}')


# a=10
# b=5
# c=a*b
# print(a,b,c)

# f1=1.5
# f2=0.5
# f3=f1*f2
# print(f1,f2,f3)

# s1="A"*10
# print(s1)

# s2="PYTHON"*2
# print(s2)

# A=[0]*20
# print(A)

# B=4*[1,2,3]
# print(B)


# Write a program to input product name, qty, price
# calculate total amount
# p_name=input("enter product name: ")
# p_quantity=int(input("enter product quantity: "))
# p_price=int(input("enter product price: "))

# print(f'Product {p_name}, Quantity {p_quantity} and Total price {p_quantity * p_price}')


# a=5
# b=2
# c=a/b
# print(a,b,c)

# n1=4
# n2=2
# n3=n1/n2
# print(n1,n2,n3)


# Write a program to find simple interest
# I=P*T*R/100
# amount=int(input("enter amount: "))
# time=int(input("enter year: "))
# rate=float(input("enter rate of interest: "))
# I=(amount*time*rate)/100
# print(f'Simple Interest: {I}')


# a=5/2
# print(a)

# b=5//2
# print(b)

# c=-5//2
# print(c)

# d=4/2
# print(d)

# e=4//2
# print(e)

# print(type(e))

# f=5.0//2


# n=int(input("enter number: "))
# l_digit=n%10
# print(f'{n} last digit is: {l_digit}')


# n=int(input("enter number: "))
# r_digit=n//10
# print(f'original number: {n}')
# print(f'after remove last digit: {r_digit}')


# a=int(input("Enter number: "))
# n=1<=a<=10
# print(n)

# ------------------------------ - ------------------------------ 
# *** conditional operator ***
# syntax: operand_1 if (condition) else operrand_2
# write a program to find max of 2 number

# n_1=int(input("Enter first Number: "))
# n_2=int(input("Enter second Number: "))
# max=n_1 if n_1>n_2 else n_2
# print(f'Max is: {max}')

# Write a program to find a person is elg to vote or not

# age=int(input("Enter Age: "))
# result= "eligible" if age>=18 else "not eligible"
# print(result)

# Write a program to find input number is 3 digit number or not

# digit=int(input("Enter a number: "))
# result= "3 digit number" if digit>=100 and digit<=999 else "not 3 digit number"
# print(result)

'''
Q. Write a program to find input letter is vowel or not
l=['A','E','I','O','U','a','e','i','o','u']
'''
# ch=input("Enter any charecter: ")
# result= "Vowel" if ch in 'AEIOUaeiou' else "not Vowel"    # in is membership operator
# print(result)
# ------------------------------ - -------------------------------
'''
*** Using multiple conditional operators ***
syntax:
var= operand_1 if (condition_1) else operand_2 if (condition_2) else operand_3 if...else...
'''

'''
Q. Write a program to input 3 number and find max
'''
# num_1= int(input("enter 1st number: "))
# num_2= int(input("enter 2nd number: "))
# num_3= int(input("enter 3rd number: "))

# max= num_1 if num_1>num_2 and num_1>num_3 else num_2 if num_2>num_1 and num_2>num_3 else num_3

# print(f'max number between {num_1}, {num_2} and {num_3} is {max}')  # this is sting version
# print(f'max number between {num_1, num_2, num_3} is {max}') # this is tuple version
# ------------------------------ - -------------------------------
'''
Q. Write a program to swap 2 numbers using bitwise operators
'''
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number: "))
# print(f'number befor swap: {a,b}')
# a=a^b
# b=a^b
# a=a^b
# print(f'number after swaping: {a,b}')
# ------------------------------ - -------------------------------
# walrus operator
# x=5
# y=2
# # z=(p=(x+y))*(q=(x-y))
# z=(p:=x+y)*(q:=x-y)
# print(p,q,z)
# ------------------------------ - -------------------------------
# num= int(input("enter any number: "))
# num1=num
# max=0
# min=0
# while num1>0:
#     # print(num1)
#     l_digit=num1%10
#     # print(l_digit)
#     if l_digit>max:
#         max=l_digit
#     if min<max:
#         min=l_digit
#     print(l_digit)
#     num1=num1//10
# print(f'Maximum digit of {num} is {max}')
# print(f'Minumum digit of {num} is {min}')


# num=int(input("enter number: "))
# num1=num
# max=0
# min=0
# while num1>0:
#     print(num1)
#     a=num1%10
#     if a>max:
#         max=a
#     else:
#         min=a
#         print()
    
#     num1= num1//10
# print(f'Maximum digit of {num} is {max}')
# print(f'Minumum digit of {num} is {min}')
# ------------------------------ - -------------------------------
# CONDITIONAL CONTROL STATEMENT
'''
Q. Write a program to find last digit Output of number is divisible with 3 or not
'''
# num=int(input("enter number: "))
# d=num%10
# if d%3==0:
#     print(f'last digit divisible by 3')
# else:
#     print(f'not divisible by 3')

'''
Q. Write a program to find input number is +ve,-ve or zero
'''
# num=int(input("enter number: "))
# if num==0:
#     print(f'{num} is zero')
# elif num>0:
#     print(f'{num} is positive')
# else:
#     print(f'{num} is negative')

'''
Q. Write a program to input single character and find alphabet, digit or special character
'''
# ch=input("enter a character: ")
# if ch>='0' and ch<='9':
#     print(f'{ch} is a Digit')
# elif ch>='a' and ch<='z' or ch>='A' and ch<='Z':
#     print(f'{ch} is a Alphabet')
# else:
#     print(f'{ch} is a Special Character')

'''
Q. Write a program to input single character and convert

* if given character alphabet and lowercase convert into uppercase
* if uppercase then convert into lowercase
'''
# ch=input("enter a character: ")
# if ch>='a' and ch<='z':
#     print(chr(ord(ch)-32))
# elif ch>='A' and ch<='Z':
#     print(chr(ord(ch)+32))
# else:
#     print("input only Alphabet")

'''
Q. write a program to calculate the electicity bill (accept number of unit from user)
according to thr following criteria:
        unit                price
    1st 100 unit          no charge
    next 100 unit       rs. 5 per unit
    after 200 unit      rs. 10 per unit
'''
# unit=int(input("enter meter unit: "))
# if unit<=100:
#     bill=0
# elif unit>100 and unit<=200:
#     bill=(unit-100)*5
# else:
#     bill=500+(unit-200)*10
# print(f'Electricity bill amount: {bill} Rs.')

'''
Q. write a program to accept the cost price of a bike and display tax to be paid according to the following criteria:
    cost price (in Rs.)         Tax
    > 100000                    15%
    > 50000 and <= 100000       10%
    <= 50000                    5%
'''
# price=int(input("\nenter price of bike: "))
# if price<=50000:
#     tax=5
#     cost=price*(tax/100)
#     total=price+cost
# elif price>50000 and price<=100000:
#     tax=10
#     cost=price*(tax/100)
#     total=price+cost
# else:
#     tax=15
#     cost=price*(tax/100)
#     total=price+cost
# print(f'\nCost Price of Bike: {price}')
# print(f'{tax}% Tax amount: {cost} Rs.')
# print(f'Total cost of Bike: {total} Rs.\n')


'''
Q. write a program login validation.
* if user_name and password correct: welcome
* if user_name incorrect: invalid username
* if password incorrect: invalid password
'''
# print("\nUSER_NAME: BLACK_STAR")
# print("PASSWORD: STAR@123\n")
# u_name=input("enter Username: ")
# if u_name=='BLACK_STAR':
#     password=input("enter Password: ")
#     if password=='STAR@123':
#         print("WELCOME")
#     else:
#         print("INVALID PASSWORD")
# else:
#     print("INVALID USER_NAME")

'''
Q. write a program to find the max of 3 number.
'''
# ------------------------- code_1 -------------------------
# # Using only if
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# max_num = a  # assume first is max
# if b > max_num:
#     max_num = b
# if c > max_num:
#     max_num = c
# print("Maximum number is:", max_num)
# ------------------------- code_2 -------------------------
# # Using if else
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b:
#     max_num = a
# else:
#     max_num = b

# if c > max_num:
#     max_num = c

# print("Maximum number is:", max_num)
# ------------------------- code_3 -------------------------
# # Using if elif else
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     max_num = a
# elif b >= a and b >= c:
#     max_num = b
# else:
#     max_num = c

# print("Maximum number is:", max_num)
# ------------------------- code_4 -------------------------
# # Using nested if
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b:
#     if a >= c:
#         max_num = a
#     else:
#         max_num = c
# else:
#     if b >= c:
#         max_num = b
#     else:
#         max_num = c

# print("Maximum number is:", max_num)
# ------------------------------ - -------------------------------
'''
MATCH CASE:

Q. write a program on ATM using match,
1. deposite
2. widrawl
3. balance check
4. exit  
it is menu driven program.
'''
# print(''' Choose one Option in the MENU
#     1. DEPOSITE
#     2. WITHDRAWL
#     3. CHECK BALANCE
#     4. EXIT 
# ''')
# a=int(input("Enter above option: "))
# a_balance=0
# match a:
#     case 1:
#         amount=int(input("enter amount: "))
#         a_balance+=amount
#         print(f'{amount} Deposite Succesfully')
#     case 2:
#         amount=int(input("enter amount: "))
#         a_balance-=amount
#         print(f'{amount} Withdwal Succesfully')
#     case 3:
#         print(f'Your Account Balance: {a_balance}')
#     case 4:
#         print(f'GoodBye...!!')
#         exit
'''
CASE WITH MULTIPLE PATTERNS:

Q. write a program to check input character is vowel or not.
'''
# ch=input("enter an alphabet: ")
# match ch:
#     case 'a'|'e'|'i'|'o'|'u':
#         print("VOWEL")
#     case 'A'|'E'|'I'|'O'|'U':
#         print("VOWEL")
#     case _:
#         print("CONSTANT")
'''
GUARDS (CONDITION if):

Q. write a program to find even or odd.
'''
# num=int(input("enter any number: "))
# match num:
#     case num if num%2==0:
#         print("Even")
#     case num if num%2!=0:
#         print("Odd")
# ------------------------------ - -------------------------------
# WHILE LOOP
'''
Q. write a program to print 1 to 10.
'''
# num=1
# while num<=10:
#     print(num, end=' ')
#     num+=1
'''
Q. write a program to print 10 to 1.
'''
# num=10
# while num>=1:
#     print(num,end=' ')
#     num-=1
'''
Q. write a program to input 5 numbers and print sum.
'''
# n=5
# sum=0
# while n>=1:
#     num=int(input("enter a number: "))
#     sum=sum+num
#     n-=1
# print(sum)
'''
Q. Write a program to input a numbers and count even and odd numbers
'''
# num=int(input("enter a number: "))
# num1=num
# ec=0
# oc=0
# while num1>0:
#     d=num1%10
#     if d%2==0:
#         ec+=1
#     else:
#         oc+=1
#     num1=num1//10
# print(f'Even Count: {ec}')
# print(f'Odd Count: {oc}')
'''
Q. write a program to generate math table of any number.
'''
# num=int(input("enter a number to print Math table: "))
# n=1
# while n<=10:
#     print(f'{num} x {n} = {num*n}')
#     n+=1
'''
Q. write a program to find factorial of a number.
'''
# num=int(input('enter any number: '))
# n=1
# fact=1
# while n<=num:
#     if num>0:
#         fact=fact*n
#     n+=1
# if num==0:
#     fact=0
# print(fact)
'''
Q. write a program to find length of number or count of digit.
'''
# num=int(input("enter a number: "))
# c=0
# while num>0:
#     c+=1
#     num=num//10
# print(f'Length of given Number is {c}')
'''
Q. Write a program to print sum of digits of a given number
'''
# num=int(input("enter number: "))
# num1=num
# sum=0
# while num1>0:
#     d=num1%10
#     sum+=d
#     num1=num1//10
# print(sum)
'''
Q. write a program to reverse input number pallindrom or not.
'''
# num=int(input("enter any number: "))
# num1=num
# a=0
# while num1>0:
#     d=num1%10
#     a=(a*10)+d
#     num1//=10
# if a==num:
#     print("Pallindrom")
# else:
#     print("not Pallindrom")
'''
Q. write a program to convert decimal to binary.
'''
# num=int(input("Enter a decimal number: "))
# num1=num
# bin=""
# while num1>0:
#     d=(num1%2)
#     bin=str(d)+bin
#     num1=num1//2
# if num==0:
#     bin=0
# print(f'Binary of {num} is 0b{bin}')
'''
Q. write a program to convert decimal to hexadecimal.
'''
# ------------------------- code_1 -------------------------
# num=int(input("enter a number: "))
# num1=num
# hex=""
# while num1>0:
#     d=num1%16
#     print(d)
#     match d:
#         case 10:
#             hex='a'+hex
#         case 11:
#             hex='b'+hex
#         case 12:
#             hex='c'+hex
#         case 13:
#             hex='d'+hex
#         case 14:
#             hex='e'+hex
#         case 15:
#             hex='f'+hex
#         case _:
#             hex=str(d)+hex
#     num1=num1//16
# if num==0:
#     hex=0
# print(f'Hexadecimal of {num} is 0x{hex}')

# ------------------------- code_2 -------------------------
# num = int(input("Enter a decimal number: "))
# hex_digits = "0123456789ABCDEF"   
# hex = ""                  
# num1 = num
# while num1 > 0:
#     r = num1 % 16
#     print(r)
#     hex = hex_digits[r] + hex
#     print(hex)
#     num1 = num1 // 16
# if num == 0:
#     hex = "0"
# print(f"Hexadecimal of {num} is: 0x{hex}")
'''
Q, write a program to convert decimal to octal.
'''
# num=int(input("enter a decimal number: "))
# num1=num
# oct=""
# while num1>0:
#     d=num1%8
#     oct=str(d)+oct
#     num1=num1//8
# if num==0:
#     oct=0
# print(f'Octal of {num} is 0o{oct}')

"""
*** NESTED WHILE LOOP ***


Q. Write a program to generate math tables from 1 to 10 using while loop
"""
# num=1
# while num<=10:
#     i=1
#     while i<=10:
#         print(f'{num} x {i} = {num*i}')
#         i+=1
#     print()
#     num+=1

'''
Q. Write a program to generate palindrome numbers from 100 to 300
'''
# print('FOR PRINT PALINDROM NUMBER INPUT A RANGE __ TO __')
# num,num2=map(int,input("enter range: ").split())
# while num<=num2:
#     num1=num
#     rev=0
#     while num1>0:
#         p=num1%10
#         rev=(rev*10)+p
#         num1=num1//10
#     if rev==num:
#         print(num)
#     num+=1


# ------------------------------ - -------------------------------
# FOR LOOP
'''
q. write a program to print math table.
'''
# num=int(input('enter a number: '))
# for i in range(1,11):
#     print(f'{num} x {i} = {num*i}')
'''
Q. write a program to find input number is prime or not.
'''
# num=int(input('enter a number: '))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print(f'Number is Prime')
# else:
#     print(f'Number is not Prime')
'''
Q. write a program to input n number and print sum.
'''
# n=int(input('enter how many number to put?: '))
# sum=0
# for i in range(n):
#     num=int(input('enter number: '))
#     sum=sum+num
# print(sum)
'''
Q. write a program to input n number and find min and max value.
'''
# n=int(input('ente how many number to put?: '))
# max=0
# min=0
# for i in range(n):
#     num=int(input('enter number: '))
#     if i==0:
#         min=num
#         max=num
#     elif num>max:
#         max=num
#     elif num<min:
#         min=num
# print(max)
# print(min)
# ------------------------------ - -------------------------------

# a,b,c=list(map(int,input().split()))
# print(a,b,c)
# or can be write without list
# a,b,c=(map(int,input().split()))
# print(a,b,c)

# ------------------------------ - -------------------------------
'''
Q. write a program to find factorial of number.
'''
# num=int(input("enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# if num==0:
#     fact=0
#     print(f'Factorial of {num}! is {fact}')
# else:
#     print(f'Factorial of {num}! is {fact}')


# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i*j}')
#     print()
# ------------------------------ - -------------------------------
'''
Q. Write a Program to print 1 to 100
'''
# for i in range(2,101):
#     c=0
#     for j in range(1,i+1):
#         if i%(j**0.5)==0: #for squar root method
#             c+=1
#     if c==1:
#         print(i)

# for i in range(2,101):
#     c=0
#     for j in range(1,i+1):
#         if i%(j**0.5)==0:
#             c+=1
#     if c==1:
#         print(i)

# ------------------------------ - -------------------------------
'''
Q. Write a program to generate armstrong number from 1 to 999.
'''
# ------------------------- code_1 -------------------------
# for num in range(1,1000):
#     num1=num
#     sum=0
#     for i in str(num1):
#         sum=sum+(int(i)**3)
#     if sum==num:
#         print(sum)
# ------------------------- code_2 -------------------------
# for num in range(1,1000):
#     num1=num
#     sum=0
#     while num1>0:
#         p=num1%10
#         sum=sum+(p**3)
#         num1=num1//10
#     if sum==num:
#         print(sum)
# ------------------------------ - -------------------------------
"""
BRANCH STATEMENT

Q. Write a program to generate sum of first 10 numbers which are divisible with 3
"""
# num=1
# sum=0
# count=0
# while True:
#     if num%3==0:
#         print(num)
#         sum+=num
#         count+=1
#     if count==10:
#         break
#     num+=1
# print(sum)

'''
Q. Write a program to find input number is prime or not.
'''
# num=int(input("enter any number: "))
# count=0
# a=int(num**0.5)
# for i in range(1,a+1):
#     if num%i==0:
#         count+=1
#     if count>1:
#         break

# if num==1:
#     print('1 is NOT a PRIME Number')
# elif count==1:
#     print('PRIME')
# else:
#     print('NOT PRIME')

# while True:
#     u_name=input("enter user name: ")
#     u_pass=input("enter your password: ")
#     if u_name=='bibek69' and u_pass=='bibek@1234':
#         print('\nWELCOME\n')
#         break
#     else:
#         print('\nINVALID USERNAME AND PASSWORD\n')

# for i in range(10):
#     print('HELLOW')
#     continue
#     print('BYE')

# for i in range(20):
#     if i%2==0:
#         continue
#     print(i)

# ------------------------------ - -------------------------------
"""
LIST
"""
'''
Q. Write a program to count alphabets,digits and special characters exists list,
A=['1','a','b','*','c','2','4','8','/','A','B']
'''
# A=['1','a','b','*','c','2','4','8','/','A','B']
# ac=0
# dc=0
# sc=0
# for i in A:
#     if i>='A' and i<='Z' or i>='a' and i<='z':
#         ac+=1
#     elif i>='0' and i<='9':
#         dc+=1
#     else:
#         sc+=1
# print('Alphabet Count is:',ac)
# print('Digit Count is:',dc)
# print('Special character is:',sc)
'''
# Write a program to print count sales, which are >=50000 and < 50000
sales=[67000,45000,55000,25000,15000,65000,80000,35000]
'''
# sales=[67000,45000,55000,25000,15000,65000,80000,35000,40500]
# s_count=0
# s_count2=0
# for i in sales:
#     if i>=50000:
#         s_count+=1
#     else:
#         s_count2+=1
# print('Sales under 50000:',s_count2)
# print('Sales above 50000:',s_count)
'''
Q. Write a program to read scores of n players and display total score,maximum score, minimum score
'''
# ----------------------- code_1 -----------------------
# num=int(input('Enter player numbers: '))
# score=list()
# for i in range(1,num+1):
#     s=int(input(f'Enter player {i} score: '))
#     score.append(s)

# # Usinf Pre-define Methods
# print(score)
# print(f'Total Scores: {sum(score)}')
# print(f'Max Score: {max(score)}')
# print(f'Min Score: {min(score)}')
'''
Q. Write a program to separate even numbers and odd numbers into separate list
A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
'''
# A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# even=[]
# odd=[]
# for value in A:
#     if value%2==0:
#         even.append(value)
#     else:
#         odd.append(value)
# print(f'List: {A}\nEven number: {even}\nOdd number: {odd}')
'''
Q. Write a program to input n elements into list and sort elements ascending order using bubble sort
'''
#------------------------ code_1------------------------
# print('\n*** Enter values with space ***')
# num=list(map(int,input().split()))

# print(f'List Befor Sort: {num}')

# for i in range(len(num)):
#     for j in range(len(num)-1):
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]

# print(f'List After Sort: {num}')

#------------------------ code_2------------------------
'''
Note: This is Optimize program of previous one if the list is sorted then the loop stop.
'''
# print('\n*** Enter values with space ***')
# num = list(map(int, input().split()))
# print("Before sorting:", num)

# n = len(num)

# for i in range(n):
#     swapped = False   # optimization flag

#     for j in range(n - i - 1):  #n - i - 1 avoids comparing elements that are already in correct position
#         if num[j] > num[j + 1]:
#             num[j], num[j + 1] = num[j + 1], num[j]
#             swapped = True

#     # if no swapping happened, list is already sorted
#     if not swapped:
#         break

# print("After sorting:", num)
#-------------------------------------------------------
'''
Q. Write a program to remove duplicate values from list
'''
A=[10,20,30,10,10,20,30,40,40,50,50,10,20]
# ----------------------- code-1 -----------------------
# b=[]
# for i in A:
#     if i not in b:
#         b.append(i)
# print(b)

# ----------------------- code-2 -----------------------
# c=[]
# i=0
# l=len(A)
# while i < l:
#     if A[i] not in c:
#         c.append(A[i])
#     i+=1
# print(c)
'''
Q. Write a program to count of each value in list
'''
# A=[10,20,30,10,10,20,30,40,40,50,50,10,20]
# b=[]
# for i in A:
#     if i not in b:
#         b.append(i)
# print(b)
# l=len(A)
# for i in b:
#     count=0
#     for j in range(l):
#         if i==A[j]:
#             count+=1
#     print(f'{i}:{count}')

# using count() method:
# for value in b:
#     c=A.count(value)
#     print(f'{value}:{c}')
'''
Q. Write a program to implement stack data structure
'''
# a=[]
# while True:
#     print()
#     print(f'1. Push')
#     print(f'2. Pop')
#     print(f'3. View')
#     print(f'4. Exit')
#     print()
#     option=int(input('Choose Option: '))
#     print()
#     match option:
#         case 1:
#             print('PUSH SINGLE/MULTI VALUE IN STACK (USE SPACE BETWEEN VALUES):')
#             a=list(map(int,input().split()))
#             print(f'Values are Push to the Stack.')
#         case 2:
#             if len(a)==0:
#                 print('Stack is Empty!!')
#             else:
#                 value=a.pop()
#                 print(f'{value} is Poped from Stack.')
#         case 3:
#             print(f'Stack: {a}')
#         case 4:
#             break
'''
Q. Write a program to find second maximum of given list values
'''
# A=[10,20,30,10,40,50,50,35]
# A.sort()
# b=[]
# for value in A:
#     if value not in b:
#         b.append(value)
# print(b)
# print(f'Second maximum value in list: {b[-2]}')
'''
Q. Write a program to create 2x2 matrix and display
'''
# a=[]
# for i in range(2):
#     b=[]
#     for j in range(2):
#         c=int(input('Enter Value: '))
#         b.append(c)
#     a.append(b)
# print(a)
# --------------------------------------------------
# A=[[1,2,3],[4,5,6],[7,8,9]]
# # Without Using Index
# for i in A:
#     for j in i:
#         print(j,end=' ')
#     print()
# print()
# # Using Index
# for i in range(3):
#     for j in range(3):
#         print(A[i][j],end=' ')
#     print()
# --------------------------------------------------
'''
Q. Write a program to print sum 2 matrices read two 2x2 matrices.
'''
# a=[]
# b=[]
# print("*** ENTER FIRST MATRIX ***")
# for i in range(2):
#     x=list(map(int,input().split()))
#     a.append(x)
# print(a)
# print("*** ENTER SECOND MATRIX ***")
# for i in range(2):
#     y=list(map(int,input().split()))
#     b.append(y)
# print(b)
# print("***ADDITION OF TWO MATRIX***")
# for i in range(2):
#     for j in range(2):
#         print(a[i][j]+b[i][j],end=' ')
#     print()
# print()
'''
Q. Write a program to read sales 3 sales persons 5 months sales
# calculate total sales
# calculate total sales-sales person wise
'''
# P=int(input('Enter Number of Person: '))
# M=int(input('Enter Number of Month/Person: '))
# Sales=[]
# for i in range(1,P+1):
#     a=[]
#     for j in range(1,M+1):
#         c=int(input(f'Enter {i} Person {j} Month Sales: '))
#         a.append(c)
#     Sales.append(a)
#     print()

# t_sale=0
# i=0     # foe count person in loop.
# for row in Sales:
#     sale=0
#     for value in row:
#         sale+=value
#     t_sale=t_sale+sale
#     i+=1
#     print(f'Person {i} Total Month Sale: {sale}')
# print(f'Total Sales of {i} Persons are: {t_sale}')

# OR we can use buit-in function 'sale=sum(value)' & have to remove inner loop to work it perfectly.

# t_sale=0
# i=0
# for row in Sales:
#     sale=sum(row)
#     t_sale+=sale
#     i+=1
#     print(f'Person {i} Total Month Sale: {sale}')
# print(f'Total Sales of {i} Persons are: {t_sale}')
'''
Q. Write a program to print upper and lower triangle of matrix
'''
# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         c=int(input('Enter a number: '))
#         b.append(c)
#     a.append(b)
# print(a)
# for i in range(3):
#     for j in range(3):
#         if i<=j:
#             print(a[i][j],end=' ')
#         else:
#             print(" ",end=' ')
#     print()
# for i in range(3):
#     for j in range(3):
#         if i>=j:
#             print(a[i][j],end=' ')
#         else:
#             print(" ",end=' ')
#     print()
'''
Q. Write a program to find inverse of 2x2 matrix
'''
# a=[[1,2],[3,4]]

'''FIND DETERMINAT AND THEN ADJOINT OF 2X2 MATRIX'''
# dt_a=(a[0][0]*a[1][1])-(a[0][1]*a[1][0])
# b=[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]
# print(f'THIS IS 2X2 MATRIX:{a}\nTHIS IS ADJOINT OF 2X2 MATRIX{b}')

'''CREATING THE INVERSE OF 2X2 MATRIX'''
# inv_mtx=[]
# if dt_a==0:
#     print("INVERSE NOT EXIST!!!")
# else:
#     for i in range(2):
#         c=[]
#         for j in range(2):
#             D=(b[i][j]/dt_a)
#             c.append(D)
#         inv_mtx.append(c)
# print(f'INVERS OF 2X2 MATRIX: {inv_mtx}')

# '''TAKING INPUT FOR 2X2 MATRIX'''
# print("*** THIS IS A 2X2 MATRIX ***")
# a=[]
# for i in range(1,3):
#     x=[]
#     for j in range(1,3):
#         y=int(input(f'ENTER ROW({i}) & COLUMN({j}): '))
#         x.append(y)
#     a.append(x)

# '''FIND DETERMINAT AND THEN ADJOINT OF 2X2 MATRIX'''
# dt_a=(a[0][0]*a[1][1])-(a[0][1]*a[1][0])
# b=[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]

# print(f'\nTHIS IS 2X2 MATRIX: {a}\n\nADJOINT OF 2X2 MATRIX: {b}')

# '''CREATING THE INVERSE OF 2X2 MATRIX'''
# inv_mtx=[]
# if dt_a==0:
#     print(f'DETERMINAT OF 2X2 MATRIX: {dt_a}')
#     print("\n2X2 INVERSE MATRIX NOT EXIST!!!")
# else:
#     print(f'DETERMINAT OF 2X2 MATRIX: {dt_a}')
#     for i in range(2):
#         c=[]
#         for j in range(2):
#             D=(b[i][j]/dt_a)
#             c.append(D)
#         inv_mtx.append(c)
#     print(f'\nINVERS OF 2X2 MATRIX: {inv_mtx}')
'''
Q. Write a program to print matrix transponse
'''
# print("*** THIS IS A 3X3 MATRIX ***")
# a=[]
# for i in range(1,4):
#     x=[]
#     for j in range(1,4):
#         y=int(input(f'ENTER ROW({i}) & COLUMN({j}): '))
#         x.append(y)
#     a.append(x)
# T_a=[]
# for i in range(3):
#     c=[]
#     for j in range(3):
#         c.append(a[j][i])
#     T_a.append(c)

# print("*** THIS IS 3X3 MATRIX ***")
# for idx in a:
#     print(idx)
# print()
# print("*** THIS IS THE TRANSPOSE OF 3X3 MATRIX ***")
# for idx in T_a:
#     print(idx)

'''
TUPLE

Q. Find the Size of a Tuple in Python

Given a tuple, the task is to find its size, i.e.,
the number of elements in it. For example:
Input: (10, 20, 30, 40, 50)
Output: 5
'''
# a=tuple(map(int,input().split()))
# print(a)
# print(len(a))
# c=0
# for i in a:
#     c+=1
# print(c)
# b=len(a)
# co=0
# while b>0:
#     co+=1
#     b-=1
# print(co)
'''
Q. Python - Maximum and Minimum K elements in Tuple

Given a tuple of numeric elements and an integer K,
the task is to find the K smallest and K largest
elements from the tuple.

Example:
Input:
t = (2, 4, 3, 6, 8, 11, 1, 9)
k=2

Output:
min = 1, 2
max = 9, 11
'''
# t = (2, 4, 3, 6, 8, 11, 1, 9)
# k=2
# print(t)
# s=tuple(sorted(t))
# print(s)
# print(s[:k])
# print(s[-k:])
'''
Q. Create a List of Tuples with Numbers and Their Cubes -Python

Given a list of numbers, the task is to create a list of
tuples where each tuple contains a number and its cube.
For example:
Input: [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]
'''
# T_list=[1,2,3]
# O_list=[]
# for i in T_list:
#     a=i,i**3
#     O_list.append(a)
#     # O_list.append((i,i**3))   # can be written like this
# print(O_list)




           


































# A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i in A:
#     B=list("i")
#     print(B)
# print(B)















# f


















# ------------------------------ - -------------------------------
# ------------------------------ - -------------------------------
# ------------------------------ - -------------------------------

# ------------------------- code_1 -------------------------
# num=int(input("enter number: "))
# num1=num
# max=0
# min=9
# while num1>0:
#     a=num1%10
#     if a>max:
#         max=a
#     if a<min:
#         min=a
#     num1= num1//10
# print(f'Maximum digit of {num} is {max}')
# print(f'Minumum digit of {num} is {min}')
# ------------------------- code_2 -------------------------
# num=int(input('enter any number: '))
# num1=num
# max=0
# min=9
# while num1>0:
#     d=num1%10
#     if d<min:
#         min=d
#     elif d>max:
#         max=d
#     num1=num1//10
# print(f'Maximum digit of {num} is {max}')
# print(f'Minumum digit of {num} is {min}')
# ------------------------- code_3 -------------------------
# num = int(input("Enter any number: "))
# s = str(num)
# i = 0
# max_digit = 0
# min_digit = 9
# while i < len(s):
#     d = int(s[i])
#     if d < min_digit:
#         min_digit = d
#     if d > max_digit:
#         max_digit = d
#     i += 1
# print(f"Maximum digit of {num} is {max_digit}")
# print(f"Minimum digit of {num} is {min_digit}")
# ------------------------- code_4 -------------------------
# num = int(input("Enter number: "))
# num1 = num
# Initialize with the last digit
# min_digit = num1 % 10
# max_digit = num1 % 10
# num1 //= 10
# while num1 > 0:
#     a = num1 % 10
#     if a > max_digit:
#         max_digit = a
#     if a < min_digit:
#         min_digit = a
#     num1 //= 10
# print(f"Maximum digit of {num} is {max_digit}")
# print(f"Minimum digit of {num} is {min_digit}")
# ------------------------- code_5 -------------------------
# num = input("Enter number: ")
# print(f"Maximum digit of {num} is {max(num)}")
# print(f"Minimum digit of {num} is {min(num)}")
# ------------------------------ - -------------------------------





        
        







# str="123"
# for i in range(1):
#     print(str.center(10,'-'))








































































# 9512476548324












# f
































