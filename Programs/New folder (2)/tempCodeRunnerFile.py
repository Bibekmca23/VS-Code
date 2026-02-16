T_list=[1,2,3]
O_list=[]
for i in T_list:
    a=i,i**3
    O_list.append(a)
    # O_list.append((i,i**3))   # can be written like this
print(O_list)