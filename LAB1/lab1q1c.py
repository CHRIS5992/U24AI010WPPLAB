list=[]
alpha = ord("a")
for i in range(1,27):
    letter= chr(alpha+i-1)   
    list.append(letter*i)
print(list)