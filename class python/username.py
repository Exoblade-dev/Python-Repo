def DOB(a):
    year=a%10000
    remainder=int(a/10000)
    month=remainder%100
    day=int(month//100)
    print(f"DOB:{day}-{month}-{year}")
    
    
a=int(input("Enter ur DOB:"))
DOB(a)