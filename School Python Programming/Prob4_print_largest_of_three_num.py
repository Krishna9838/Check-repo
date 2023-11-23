# user input
a=eval(input("Enter first num: "))
b=eval(input("Enter second num: "))
c=eval(input("Enter third num: "))

# Process
if a<b:
    if b<c:
        print(c," is maximum")
    else:
        print(b," is maximum")
else:
    print(a)
    
