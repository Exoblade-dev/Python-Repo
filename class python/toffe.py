import random 
def chocolate_distribution():
    chocolates =0
    count =0
    crying=True
    
    while crying !=False:
        given =random.randint(1,10)
        khaliya=random.randint(1,5)
        
        chocolates +=given
        count +=1
        totalchocolates=chocolates-khaliya
        print(f"Uncle gave{given} ,Total chocolates ={totalchocolates}")
        print(f"child eat chocolates ={khaliya}")
        if chocolates >=20:
            crying=False
    
    
        
    print("\n child got at least 20 chocolates!")
    print("Uncle had to give chcolates ",count,"times")
    
    
chocolate_distribution()



