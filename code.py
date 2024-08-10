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
