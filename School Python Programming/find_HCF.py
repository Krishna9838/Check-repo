def findHcf(num1,num2):
    if num1>num2:
        small=num2
    else: 
        small=num1
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            HCF=i
    return HCF

a=int(input("Enter your first number here: "))
b=int(input("Enter your second number here: "))
print("Your HCF is :",findHcf(a,b))
