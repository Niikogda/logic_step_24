
x=int(input("enter first number: "))
y=int(input("enter second number: "))
z=int(input("enter third number: "))
a=input("choose your action: max, min or average: ")
if a == ("max"):
    if x>z and x>y:
        print(int(x))
    elif y>x and y>z:
        print(int(y))
    elif z>y and z>x:
        print(int(z))
    else: print("mistake in the first task")
elif a == ("min"):
    if x<y and x<z:
        print(int(x))
    elif y<x and y<z:
        print(int(y))
    elif z<y and z<x:
        print(int(z))
    else:
        print("mistake in the second task")
elif a == ("average"):
    print(int((x+y+z)/3))
else:
    print("i don`t understand you, sorry;))")

