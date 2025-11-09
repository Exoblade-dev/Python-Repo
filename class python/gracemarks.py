# marks=[10,20,30,40,50,60,70,80,90,100,20,40,60,10,100,30,60,90,40,80,50,100]


    
# for mark in marks:
#     if(mark<20):
#         i=marks.index(mark)
#         marks[i]=20

# for mark in marks:
#     print(mark)
    
marks=[10,20,30,40,50,60,70,80,90,100,20]
marks.append(76)
print(marks)
marks.extend(56,78,45)
print(marks)
marks.insert(0,34)
print(marks)
marks.remove(20)
print(marks)

