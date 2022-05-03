n = input("Enter a string: ")
swap = n[-1:] + n[1:-1] + n[:1]
if len(n) == 1:
    print(n)
elif len(n) == 0:
    print("Null string")
else:
    print("The string after exchanging first and last characters:", swap)
