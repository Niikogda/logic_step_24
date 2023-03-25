
x=int(input("enter first number: "))
y=int(input("enter second number: "))
z=int(input("enter third number: "))
a=input("choose sum or prod: ")
if a == ("sum"):
    print(int(x+y+z))
elif a == ("prod"):
    print(int(x*y*z))
else:
    print("you made a mistake, sorry;)")