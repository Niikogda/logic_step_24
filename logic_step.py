
x=int(input("enter first number: "))
z=input("enter an action: ")
y=int(input("enter second number: "))
if z == ("+"):
    print(int(x+y))
elif z== ("-"):
    print(int(x-y))
elif z == ("*"):
    print(int(x*y))
elif z == ("/"):
    print(int(x/y))
else:
    print("i don`t understand you, sorry")