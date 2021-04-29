r=int(input())
l,l1,l2=[],[],[]
for i in range(1,r+1):
    
    a,b=map(int,input().split(","))
    l1.append(a)
    l2.append(b)
    
for i in range(1,max(l2)):
    count=0
    for j in range(0,r):
        if i>=l1[j] and i<l2[j]:
            count+=1
    l.append(count)
    
print(max(l))
