dictionary={}
flag=2
print("     PRODUCT DATABASE ")
while(flag==2):
    product_name= input("\nEnter Product Name = ")
    product_prices=float(input("Enter price ="))
    dictionary.setdefault(product_name,product_prices)
    flag = int(input("PRESS 2 TO ENTER NEW ENTRY\nPRESS ANY OTHER KEY TO STOP ADDING ENTRIES\n "))

print("DATABASE FINDER")
flag=2
while(flag==2):
    product_name= input("\nEnter Product Name = ")
    print(f"PRODUCT = { product_name} , PRICE = {dictionary[product_name]}")
    flag = int(input("PRESS 2 TO KEEP FINDING ENTRIES\nPRESS ANY OTHER KEY TO STOP FINDING ENTRIES\n "))



