r=int(input())
c=int(input())
n=list(map(int,input().split(",")))
a=len(n)
n1=n
print(n1,n)
l1,l2,l3=[],[],[]
res=res1=0
for i in range(0,c):
    l2=[]
    while i<a:
        
        l2.append(n1[i])
        i+=c
    l3.append(l2)
print(l3)

for i in range(0,c):
    j=0
    l=[]
    while j<r:
        
        l.append(n[0])
        #print(l)
        n.pop(0)
        #print(":",n)
        j+=1
    l1.append(l)
print(l1)
for i in range(0,r):
    s=sum(l1[i])
    if s>res:
        res=s
for i in range(0,r):
    s=sum(l3[i])
    if s>res1:
        res1=s
print(res+res1)
