def word_replace(string): 
    words = string
    print words.find("day")
    print words.replace("day", "month", 1)
word_replace("It's Thanksgiving day! It's my birthday, too!")

def min_max(list):
    x = list
    print min(x)
    print max(x)
min_max([2,54,-2,7,12,98])

def first_last(aList):
    x = aList
    newList = []
    print x[0], x[-1]
    newList.append(x[0])
    newList.append(x[-1])
    print newList
first_last(["hello",2,54,-2,7,12,98,"world"])

def newList(aList):
    tempList = []
    x = aList
    y = len(x)/2
    x.sort()
    tempList.append(x[0:y])
    x = tempList + x[y:]
    print x
newList([19,2,54,-2,7,12,98,32,10,-3,6])