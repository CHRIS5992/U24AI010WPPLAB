orignum = int(input("Enter Your Number to Find the Digital Root: "))

gg = orignum

while gg >= 10:  
    sum_of_digits = 0
    while gg > 0:
        sum_of_digits += gg % 10
        gg //= 10
    gg = sum_of_digits

print(f"Digital Root = {gg}")
