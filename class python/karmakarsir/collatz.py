n=int(input("Enter a number:")) 

# while(n==1):
#     if(n%2==0):
#      n=n/2
#     print(n)
# else:
#     n=(n*3)+1
#     print(n)
def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:   # even
            n = n // 2
        else:            # odd
            n = 3 * n + 1
        seq.append(n)
    return seq

print(collatz_sequence(n))



