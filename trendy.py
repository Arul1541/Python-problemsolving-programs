
# trendy 

l=int(input("lower:"))
u=int(input("upper:"))
for i in range(l,u):
    dig=0
    mul=1
    sum=0
    res=0
    temp=int(i)
    while temp>0:
        dig=temp%10
        mul*=dig
        sum+=dig
        temp=temp//10
    res=sum+mul
    if res==i:
        print(i)
    



