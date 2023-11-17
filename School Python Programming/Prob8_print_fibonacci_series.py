# user input
a=0
b=1
c=int(input("Enter nth term: "))
print(a,"\t")
print(b,"\t")
for i in range(1,(c-1)):
    d=a+b
    a=b
    b=d
    print(d,"\t")





