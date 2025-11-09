import math

a,b=map(int,input("Enter two integer no:").split())
c=math.pow(a,b)
d=math.exp(a)
e=math.log(a)
f=math.factorial(a)
g=math.gcd(a,b)
h=math.lcm(a,b)

print("1st number power 2nd number is:",c)
print("Exponetial of 1st number is",d)
print("Logartimic of 1st number is",d)
print("Factorial of 1st number is:",f)
print("GCD of two entered number is:",g)
print("LCM of two entered number is ",h)
