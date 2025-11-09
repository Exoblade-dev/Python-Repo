n=int(input("Enter the Fibonacci series:"))
a=0
b=1
count=0
while n>count:
    print(a,end=" ")
    a,b=b,a+b
    count=count+1