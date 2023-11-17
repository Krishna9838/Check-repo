# user input
a=input("Enter for: Fohrenheit(F) or Celsius(C) :")


if a=='C' or a=='c':
    C=eval(input("Enter value in celsius: "))
    c=(C*9/5)+32
    print(f"Your celsius temp is {c}")
elif a=='F' or a=='f':
    F=eval(input("Enter value in fohrenheit: "))
    f=(F-32)*5/9
    print(f"Your fohrenheit temp is {f}")
else:
    print("Not a valid operation")
    
