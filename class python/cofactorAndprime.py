n=int(input("Enter a number:"))
li=[]
for i in range(2,n):
    if(n%i==0):
        li.append(i)
        
        
print(li)
primeLi=[]
compositeLi=[]


for i in li:
    is_prime=True
    for j in range (2,int(i**0.5)+1):
        if (i % j  ==0):
            is_prime=False
            compositeLi.append(i)
            break
    if is_prime:
           primeLi.append(i)
        

print(f"composite factor of {n} is {compositeLi}")
print(f"prime factor of {n} is {primeLi}")

