

def square(start,end):
    count=0
    if 1 in range(start,end):
        count+=1
    for i in range(start,end+1):
   
        for j in range(2,i):
           
            if i/j == float(j)  :
                print(i,"//",j,"==",j)
                count+=1
    print(count)
a,b=int(input("enter start : ")),int(input("Enter end : "))
square(a,b)