lower=int(input("Enter lower number: "))
upper=int(input("Enter upper number: "))

for num in range(lower,upper+1):
    sum=0
    temp=num
    order=len(str(num))
    while temp>0:
        digit=temp%10
        dig=digit**order
        sum=dig+sum
        temp//=10
    if num==sum:
        print(num)
