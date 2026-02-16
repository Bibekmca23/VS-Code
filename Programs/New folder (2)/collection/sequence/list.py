'''
Sequence Data type:

List
'''
# a=list()
# x=[]
# for i in range(10,60,10):
#     a.append(i)
#     print('\n',a)
#     x.append(a)   # Using reference of a or adress of a
#     print(x)

# print(a)
# print(x)

# a=list()
# x=[]
# for i in range(10,60,10):
#     x.append(a)
#     print('\n',x)
#     a.append(i)
#     print(a)

# A=[10,20,30,40,50]
# a=list()
# x=[]
# for i in A:
#     a.append(i)
#     print('\n',a)
#     x.append(a[::]) # Using Slice method
#     print(x)

'''
Q. Write a program to print sum of elements of the following list,

A=[5,10,78,30,54,26,95,30,90,100,77,45,23]
'''
# A=[5,10,78,30,54,26,95,30,90,100,77,45,23]
# B=[1,2,3,4,5]
# A_sum=0
# B_sum=0
# for i in A:
#     A_sum+=i
# print(A_sum)
# for j in B:
#         B_sum+=j
# print(B_sum)
'''
Q. Write a program count even and odd numbers in given list.
A=[6,9,2,11,35,23,17,97,68,53,47,52]
'''
# A=[6,9,2,11,35,23,17,97,68,53,47,52]
# ec=0
# oc=0
# for i in A:
#     if i%2==0:
#         ec+=1
#     else:
#         oc+=1
# print(f'Even number: {ec}')
# print(f'Odd number: {oc}')

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

# ----------------------- code_2 -----------------------
# num=int(input('Enter player numbers: '))
# score=list()
# summ=0
# print()
# for i in range(1,num+1):
#     s=int(input(f'Enter player {i} score: '))
#     score.append(s)

# maxx=score[0]
# minn=score[0]
# for i in range(len(score)):
#     if score[i]>=maxx:
#         maxx=score[i]
#     if score[i]<minn:
#         minn=score[i]
#     summ+=score[i]
# print(f'\nTotal Score of Playes are: {summ}')
# print(f'Maximum score of player: {maxx}')
# print(f'Minimum score of player: {minn}')

# ----------------------- code_3 -----------------------
# print(f'\n*** ENTER SCORE OF PLAYER ***')
# score=list(map(int,input().split()))
# print(score)
# mini=score[0]
# maxi=score[0]
# total=0
# for i in range(len(score)):
#     if score[i]>maxi:
#         maxi=score[i]
#     if score[i]<mini:
#         mini=score[i]
#     total=total+score[i]
# print(f'\nTotal Score of Playes are: {total}')
# print(f'Maximum score of player: {maxi}')
# print(f'Minimum score of player: {mini}')

# ----------------------- code_4 -----------------------
# print(f'\n*** ENTER SCORE OF PLAYER ***')
# score=list(map(int,input().split()))
# print(f'You have entered {len(score)} Players Score:')
# print(score)
# mini=score[0]
# maxi=score[0]
# total=0
# for value in score:
#     if value>maxi:
#         maxi=value
#     if value<mini:
#         mini=value
#     total+=value
# print(f'\nTotal Score of Playes are: {total}')
# print(f'Maximum score of player: {maxi}')
# print(f'Minimum score of player: {mini}')
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
# ----------------------- code-1 -----------------------
# A=[10,20,30,10,40,50,50,35]
# A.sort()
# b=[]
# for value in A:
#     if value not in b:
#         b.append(value)
# print(b)
# print(f'Second maximum value in list: {b[-2]}')

# ----------------------- code-2 -----------------------
# A=[10,20,30,10,40,50,50,35]
# A.sort()
# F_max=A[-1]
# C=A.count(F_max)
# S_max=A[-(C+1)]
# print(f'{A}\nFirst Max number: {F_max}\nSecond Max number: {S_max}')
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
# ----------------------- code-1 -----------------------
# THIS CODE IS ONLY FOR 3-PERSON AND 5-MONTHS.

# Sales=[]
# for i in range(1,4):
#     a=[]
#     for j in range(1,6):
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

# ----------------------- code-2 -----------------------
# THIS CODE IS FOR N-PERSON AND N-MONTHS.

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

# # Using buit-in function "sale=sum(value)" & have to remove inner loop to work it perfectly.

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
# ----------------------- code-1 -----------------------
# a=[[1,2],[3,4]]

# '''FIND DETERMINAT AND THEN ADJOINT OF 2X2 MATRIX'''
# dt_a=(a[0][0]*a[1][1])-(a[0][1]*a[1][0])
# b=[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]
# print(f'THIS IS 2X2 MATRIX:{a}\nTHIS IS ADJOINT OF 2X2 MATRIX{b}')

# '''CREATING THE INVERSE OF 2X2 MATRIX'''
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

# ----------------------- code-2 -----------------------
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
# ----------------------- code-1 -----------------------
# print("*** THIS IS A 3X3 MATRIX ***")
# a=[]
# for i in range(1,4):
#     x=[]
#     for j in range(1,4):
#         y=int(input(f'ENTER ROW({i}) & COLUMN({j}): '))
#         x.append(y)
#     a.append(x)

# TRANSPOSE OF MATRIX
# b=[[a[0][0],a[1][0],a[2][0]],[a[0][1],a[1][1],a[2][1]],[a[0][2],a[1][2],a[2][2]]]

# for idx in a:
#     print(idx)
# print()
# for idx in b:
#     print(idx)

# ----------------------- code-2 -----------------------
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
Q. Write a program where
'''
# print('\n*** Enter values with space ***')
# num=list(map(int,input().split()))
# # num=[20,10,5,70,50,60,40,30]
# n=len(num)
# result=[]
# for i in range(len(num)):
#     count=0
#     for j in range(i,len(num)):
#         if num[i]>=num[j]:
#             count+=1

#     if count==n:
#         result.append(num[i])
#     n-=1
# print(result)











# a=[]
# x=()
# for i in range(1,10):
#     a.append(i)
#     x=tuple(a)
# print(a)
# print(x)
# b=x[::-1]
# print(b)
