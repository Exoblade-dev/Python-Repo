a=int(input("Enter the length of 1st side trianle:"))
b=int(input("Enter the length of 2nd side trianle:"))
c=int(input("Enter the length of 3rd side trianle:"))

if(a==b and b==c):
    print("Triangle is equilatral.")
elif(a==b or b==c or c==a):
    print("Triangle is isocesles.")
else:
    print("Triangle is Scalene.")