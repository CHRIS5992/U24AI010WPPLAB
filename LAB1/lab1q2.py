import random
randomnum= [random.choice([0,1])for i in range(100)]
maxzeros=0
currentzeros=0
minzeroes=0
list= []
for number in randomnum:
    if number ==0 :
        currentzeros+=1
        maxzeros=max(maxzeros,currentzeros)
        
    else:
        currentzeros=0

print("Longest Run of Zeros:", maxzeros)
print("Smallest Run of Zeros:", minzeroes)