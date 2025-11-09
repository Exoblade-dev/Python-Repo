

def check_anagrams(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    return(sorted(str1)==sorted(str2))


str1=(input("Enter 1st string:"))
str2=(input("Enter 2nd string:"))
if check_anagrams(str1,str2):
    print("String are aangrams.")
else:
    print("not a anograms.")