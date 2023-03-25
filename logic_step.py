
x=float(input("enter amount of meters: "))
y= input("Convert to (miles, inches, yards): ")
if y==("miles"):
    print(float(x/1609.344))
elif y==("inches"):
    print(float(x*39.37))
elif y==("yards"):
    print(float(x*1.0936))
else:
    print("mistake")