
def checkSameChar(partA,partB):
    sameChars = []
    for ltr in partA:
        if partB.find(ltr) >= 0:
            try:
                sameChars.index(ltr)
            except:
                sameChars.append(ltr)
    return sameChars

def checkSameBadge(arr):
    for ltr in arr[0]:
        if arr[1].find(ltr) >= 0:
            if arr[2].find(ltr) >= 0:
                return ltr

def giveValue(ltr): 
    if ord(ltr) > 96:
        return ord(ltr)-ord('a') + 1
    else:
        return ord(ltr)-ord('A') + 27

def problem3partA(listA):
    sumPriority = 0
    for l in listA:
        lengd = len(l)
        partA = l[0:int(lengd/2)]
        partB = l[int(lengd/2):lengd]
        same = checkSameChar(partA,partB)   
        for ltr in same:
            sumPriority += giveValue(ltr)
    print(sumPriority)

def problem3partB(listA):
    elfgroup = []
    score = 0
    for l in listA:
        elfgroup.append(l)
        if len(elfgroup) == 3:
            ltr = checkSameBadge(elfgroup)
            score += giveValue(ltr)
            elfgroup = []
        
    print(score)

#file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem3-Example.txt','r')
file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem3-Input.txt','r')

all = file.read().splitlines()

problem3partA(all)
problem3partB(all)
