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
