marks =[]
total =0
avg =0.00
count =0

def submarks():
    print("Enter the marks: ")
    for i in range(6):
        marks.append(int(input()))
    return marks*100
def caltotal():
    total =0
    avg =0.00
    count =0
    for i in marks:
        total+=i
        avg = total/len(marks)
        if avg >= 90.0:
            print("good marks")

        elif avg >= 65.0 and avg < 75.0:
            print("average marks-GIVE A CHANGE")

        elif avg < 65.0:

            print("ur fail")
def grade():
    count=0
    for i in marks:
        if marks[i] >90.0:
            count+=marks[i]
            if count>=3:
                print(" you will get gold medal")
        else:
            print("try for next chance")

submarks()
caltotal()
grade()

