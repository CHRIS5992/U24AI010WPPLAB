\
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
for i in range(1,10001):
    rem=i%5
    if rem==0:
        L1.append(i)
    elif rem==1 :
        L2.append(i)
    elif rem==2 :
        L3.append(i)
    elif rem==3 :
        L4.append(i)
    elif rem==4 :
        L5.append(i)
if set(L1+L2+L3+L4+L5) == set(range(1, 10001)) : #<- note
    print("Equivalance classes are valid")
    
