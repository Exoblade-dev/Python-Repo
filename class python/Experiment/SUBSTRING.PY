# str1=(input("Enter a string:"))
# str2=(input("Enter substring: "))
# print(str2 in str1)
import re
str1=(input("Enter a string:"))
str2=(input("Enter substring: "))

if re.search(str2,str1):
    print("substring present in string.")
else:
    print("substring not present in string.")
