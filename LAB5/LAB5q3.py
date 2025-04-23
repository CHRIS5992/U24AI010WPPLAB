inword = input("Enter Word To Lexographically Order = ")
ans = ""
max1 = inword[0]  
length = len(inword)

while length != 0:  
    max1 = inword[0] 
    for letter in inword:
        if letter > max1:
            max1 = letter  
    ans += max1  
    inword = inword.replace(max1, "", 1)  
    length -= 1  

print(f"word is = {ans}")
