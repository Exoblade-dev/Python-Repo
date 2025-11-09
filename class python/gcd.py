import math

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

result = math.gcd(a, b)
print("GCD of", a, "and", b, "is", result)

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# print("GCD of 12 and 18 is", gcd(12, 18))
