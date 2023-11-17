lower=int(input("Enter lower number here: "))
upper=int(input("Enter upper number here: "))
for num in range(lower,upper+1):
    temp=num
    sum=0
    order=len(str(num))
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)