char =input("Enter a character:")
if len(char)==1:
    if char.isdigit():
        print("Character is digit")
    elif char.islower():
        print("Character is lowercase")
    elif char.isupper():
        print("Character is uppercase")
    else:
        print("Chracter is symbol")
        
        
            
            
 
else:
     print ("Enter exactly one character.")  