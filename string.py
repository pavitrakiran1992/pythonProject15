lst1 = []

lst1 = [int(item) for item in input("Enter the list items : ").split()]
# initializing substring
subs = 'Geek'

# using filter() + lambda
# to get string with substring
res = list(filter(lambda x: subs in x, lst1))

# printing result
print("All strings with given substring are : " + str(res))



