

#fibonacci

l=int(input("lower"))
u=int(input("upper"))
n=u
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    if sum>l and sum<u:
        print(sum, end = " ")
    count+=1
    a = b
    b = sum
    sum = a + b