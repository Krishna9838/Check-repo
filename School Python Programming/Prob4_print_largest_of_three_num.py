# user input
a=eval(input("Enter first num: "))
b=eval(input("Enter second num: "))
c=eval(input("Enter third num: "))

# Process
if a>b:
    if a>c:
        print(a," is maximum")
    else:
        print(c," is maximum")
else:
    if b>c:
        print(b," is maximum")
       
    else:
        print(c," is maximum")
