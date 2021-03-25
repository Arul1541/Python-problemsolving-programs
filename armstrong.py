
# armstrong

l=int(input("lower:"))
u=int(input("upper:"))
digit=0
sum=0
n=input("number")
le=len(n)
if int(n)>=l and int(n)<=u:
    temp = int(n)
    while temp > 0:
        digit = temp % 10
        sum += digit ** int(le)
        temp //= 10


    if sum==int(n):
        print("Armstrong number")
    else:
        print("Not Armstrong number")
else:
    print("invalid input")
  