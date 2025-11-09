import math
a,b,c=map(int,input("Enter three number:").split())
if(a==0):
    print("Entered equation is not a quadtratic equation.")  
d=math.sqrt(b)-4*a*c
if(d>0):
    print("Roots of entered equation is real.")
elif(d==0):
    print("Both roots of entered equation is same and real number.")
elif(d<0):
     print("Roots of entered equation is complex number.")

    
