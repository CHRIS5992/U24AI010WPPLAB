value=float(input("FEET CONVERTER\n\nEnter your measurement in feet= "))
option=int(input("\n Enter The Desired Conversion \n [1]Feet to inches\n [2]Feet to yards\n [3]Centimetres "))
conversion=[12,1/3,30.48]
conversionname=["inches","yards","centimetres"]
print(f"{value} Feet = {conversion[option-1]*value} {conversionname[option-1]} ")