
trials = int(input("Enter Number Of Entries = "))
list = []

# Collecting the numbers
for i in range(trials):
    num = int(input("Enter Your Number = "))
    list.append(num)

print("Entered Numbers:", list)


for num in list:
    term1, term2 = 0, 1
    flag = False
    while term2 < num:
        temp = term2
        term2 = term1 + term2
        term1 = temp
    if num == term1 or num == term2:
        flag = True

    if flag:
        print(f"IsFibo")
    else:
        print(f"IsNotFibo")
