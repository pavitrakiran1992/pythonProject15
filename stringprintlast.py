n = str(input("Enter the string"))
if (len(n) < 3):
    print(n)
else:
    m=(n[0:2]+n[-2:])
    print("The first & last two characters of the string: ",m)
    print("String after removing first and last characters:", n[1:-1])#removing first and last characters