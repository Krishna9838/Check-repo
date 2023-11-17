num=int(input("Enter the num: "))
r=num**0.5
i=2
for i in range(2,num):
    if(i>r):
        print("Its a prime number")
        break
    if(num%i==0):
        print("number is not prime")
        break
    i=i+1