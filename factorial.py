#factorial
f=1
l=int(input("lower"))
u=int(input("upper"))
if l>0 and u>0:
    for i in range(u,l-1,-1):
        f=i*f
    print(f)
elif l==0 or u==0:
    print("1")
elif l<0 or u<0:
    print("invalid input")
