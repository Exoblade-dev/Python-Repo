# a=[1,2,3,4,5,6,8]
# even=[]
# for i in a:
#     if(i%2==0):
#         even.append(i)
#         i+=1
         
        
# print(even)

a=[1,2,3,4,5,6,8]
# even=[]
# for i in range(0,len(a)):
#     if(a[i]%2==0):
#         even.append(a[i])
#         i+=1
        
         
        
# print(even)


#comprehension
b=[num for num in a if num%2 ==0 ]
print(b)
