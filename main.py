def myfun(n):
    n.sort(reverse=True)
    a = sum(n)/len(n)
    b= sum(n[:4])/len(n[:4])
    c =sum(n[-3:])/len(n[-3:])
    if ((a>90) and (b>90)):
        print("GOOD MARKS AND GIVE GOLD MEDAL")
    elif ((a>90) and (b<90)):
        print ("GOOD BUT NO MEDAL")
    elif a in range(65) and c<60:
        print("GIVE OTHER CHANGE BUT FAILED")
    elif a in range(65)and c>60:
        print('GIVE OTHER CHANCE BUT PASSED') 
    else:
        print("failed")
myfun([90,95,96,90,90,92])
