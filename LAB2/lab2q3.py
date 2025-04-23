num=int(input("Enter Number Of Inputs= "))
list=[]
for i in range(num):
    entry= int(input("Enter Your Number : "))
    list.append(entry)
print(list)

for i in list:
    count=0
    x=i
    while(i>0):
        q=i%10
        i=i//10
        if q!=0:
            if (x%q==0):
                count+=1
    print(count)    
