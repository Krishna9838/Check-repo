# User input
num=int(input("Enter the number which you want to check: "))
flag=False
if num==1:
    print(f"{num} is not prime")
elif num>1: 
    for n in range(2,num):
        if num%n==0:
                flag=True
                
                break
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")

