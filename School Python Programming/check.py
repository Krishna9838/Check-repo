# # Palindrome number
# num=int(input("Enter a number: "))
# pal=str(num)
# revese_pal=pal[::-1]
# if pal==revese_pal:
#     print("The number is palindrome number")
# else:
#     print("The number is not palindrome number")

# #armastrong number
# lower=int(input("Enter a number here: "))
# upper=int(input("Enter a number here: "))

# for i in range(lower,upper+1):
#     y=str(i)
#     temp=i
#     z=len(y)
#     sum=0
#     while temp>0:
#         digit=temp%10
#         power=digit**z
#         sum=sum+power
#         temp=temp//10
#     if i==sum:
#         print(i)


# def fib(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for num in range(1,x-1):
#         c=a+b
#         a=b
#         b=c
#         print(c)
    
# a=int(input("Enter a number here: "))
# print(fib(a))

import calendar
a=int(input("Enter year: "))
b=int(input("Enter month: "))
x=calendar.month(a,b)
print(x)


        
        

    