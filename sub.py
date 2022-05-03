input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split(',')
print(user_list)
subs = input("enter the substring")
res = list(filter(lambda x: subs in x, user_list))

# printing result
print("All strings with given substring are : " + str(res))
