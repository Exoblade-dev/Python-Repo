def find_length (str):
    count=0
    for i in str:
        count=count+1
    return count

string=input("Enter the string:")
length= find_length(string)
print(length)