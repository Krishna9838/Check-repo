# # Factorail using Iteration

# # input a number
# num=int(input("Enter a number:  "))

# # Define factorial first
# fact=1

# # Difine condition
# if num<0:
#     print("No value exist")
# if num==0:
#     print("The factorial of 0 is 1")
# if num>1:
#     for i in range(1,num+1):
#         fact*=i

# # For output
# print(f"The factorial of {num} is {fact}")



# # Factorial using recursion
# def fact(num):
#     if num==0:
#         return 1
#     else:
#         return(num*(fact(num-1)))

# num=int(input("Enta a number here: "))  
# result=fact(num)
# print(f"The factorial of {num} is {result}")