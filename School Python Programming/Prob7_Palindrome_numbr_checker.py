a=int(input("Enter the number here: "))
n=str(a)
reverse_str=n[::-1]
if n==reverse_str:
    print("The number is palindrome number")
else:
    print("The number is not palindrome number")