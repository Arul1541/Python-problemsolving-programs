a=input().split()
n=len(a)-1
sum=i=0
while i<len(a)-1:
    sum+=int(a[i])
    i+=int(a[i])
if sum==n:
    print("yes")
else:
    print("No")