def average():
    sum = 0
    for i in range(num):
        sum += marksInFDS[i]
    print("Average of the Marks is:", sum/num)
    repeat()

def Maximum():
    i = 0
    max = marksInFDS[i]
    for i in range(num):
        if(marksInFDS[i] > max):
            max = marksInFDS[i]
    print("The highest score is:", max)

def Minimum():
    i = 0
    min = marksInFDS[i]
    for i in range(num):
        if(marksInFDS[i] < min):
            min = marksInFDS[i]
    print("The lowest score is:", min)
    repeat()

def absentcount():
    count = 0
    for i in range(num):
        if marksInFDS[i] == 0:
            count += 1
    print("Number of Students absent in the test : ", count)
    repeat()

def maxFrequency():
    freq = 0
    res = marksInFDS[0]
    for i in marksInFDS:
        mfreq = marksInFDS.count(i)
    if mfreq > freq:
        freq = mfreq
        res = i
    print ("Most frequent number is : " + str(res))
    repeat()

def repeat():
    ch=int(input("\nEnter your Choice: "))
    if ch == 1:
        average()
    elif ch == 2:
        Maximum()
        Minimum()
    elif ch == 3:
        absentcount()
    elif ch == 4:
        maxFrequency()
    elif ch == 5:
        print("Thank you!!")
    else:
        print("!!Invalid Input!!")

marksInFDS=[]
num=int(input("Enter total number of students: "))
print("Enter '0' for absent students")
for i in range(num):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    marksInFDS.append(marks)

print(20*"-","\n \tMENU\n",20*"-")
print("1. Average Marks of the Class")
print("2. Highest and Lowest Marks in the Class")
print("3. Number of Students absent for the test")
print("4. Marks with Highest Frequency")
print("5. Exit")

repeat()
