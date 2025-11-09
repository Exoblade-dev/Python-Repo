a=int(input("Enter(only 0 & 1) 1st number:"))
b=int(input("Enter(only 0 & 1) 2nd number:"))
c=int(input("Enter(only 0 & 1) 3rd number:"))

if((a==1 and b==1) or (a==1 and c==1) or (b==1 and c==1)):
    print("True")
else:
    print("False") 