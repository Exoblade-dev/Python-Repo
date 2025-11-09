def calculate (a,b):
    add =a+b
    sub=a-b
    mul=b*a
    div=a/b
    return add,sub,mul,div
    
x,y,z ,t=calculate(10,5)
print("Adiition:",x)
print("Subtraction",y)
print("Multiplication:",z)
print("Division:",t)