num=int(input("Enter a number here: "))
length=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    dig=digit**length
    sum=sum+dig
    temp//=10

if sum==num:
    print("This number is armstrong number")
else:
    print("This number is not armstrong number")