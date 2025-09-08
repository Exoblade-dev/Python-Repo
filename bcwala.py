import random

def chocolate_distribution():
    chocolate = 0
    count = 0
    crying = True
    
    while crying != False:
        given = random.randint(1,10)
        chocolate += given
        count += 1
        consume = random.randint(0,5)
        chocolate -= consume
        print(f"Uncle gave {given}, Total Chocolate = {chocolate}")
        print(f"child consume {chocolate} chocolates")
        if chocolate >= 20:
            crying = False
        
    print("\nChild got atleast 20 chocolate")
    print("\nUncle had to give chocolates", count , "times")
    
chocolate_distribution()