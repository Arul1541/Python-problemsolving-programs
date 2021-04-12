#odd position uppercase
'''
a=input()
l=len(a)
b=''
print(l)
for i in range(0,l):
    if i%2==0:
        b=b+a[i]
    else:
        b+=a[i].upper()
print(b)'''
#read a string and print the consisttuvie vowels word
'''a=input().split(" ")
#print(a)
l=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    #print(i)
    #print(len(i))
    count=0
    for j in (i):
        #print(j)
        count+=1
        if count<len(i):
            if j in l and i[count] in l:
                print(i)
                break'''
#read a string display the word end with s
'''a=input().split(" ")
for i in a:
    if i.endswith('s') or i.endswith('S'):
        print(i)'''
        
        
        
p=input(" para: ")
a=input("Enter the word: ")
l1=len(p)
b=''
print("initial len:",l1)
l2=len(a)
r=0
c=p.count(a)
while c>=1:
    b=a[]
    r+=c
    p=p.replace(a,'')
    print(p)
    c=p.count(a)
print("Removed:",r)
print("Result len",len(p))
print("concatenation:",con)

'''
if l2>1:
    for i in range(0,l2):
        for j in range(0,l1):
            if p[j]==a[i]:
                w=0
                k=j+1
                m=i+1
                
                while w!=1 and m<l2:
                    if p[k]==a[m]:
                        
                    
                count+=1
                
        
'''