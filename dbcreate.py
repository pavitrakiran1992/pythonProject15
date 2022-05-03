class Student:
    def __init__(self):
            pass
    def myfun(n):
        n.sorted(reverse=True)
        avg = sum(n) / len(n)
        best = sum(n[:4]) / len(n[:4])
        least = sum(n[-3:]) / len(n[-3:])
        if ((avg > 90) and (best > 90)):
            print("GOOD MARKS AND GIVE GOLD MEDAL")
        elif ((avg > 90) and (best < 90)):
            print("GOOD BUT NO MEDAL")
        elif avg in range(65) and least < 60:
            print("GIVE OTHER CHANGE BUT FAILED")
        elif avg in range(65) and least > 60:
            print('GIVE OTHER CHANCE BUT PASSED')
        else:
            print("failed")
s1 = Student()
s1.myfun([90, 95, 96, 90, 90, 92])

# It will produce the final output
print ("\nThe Total marks is:   ", s1.sum(n))
print ("\nThe Average marks is: ", s1.avg(n))

