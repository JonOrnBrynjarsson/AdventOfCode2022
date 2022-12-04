

def contains(aMin,aMax,bMin,bMax) -> int:    
    if aMin >= bMin and aMax <= bMax:
        return 1
    elif bMin >= aMin and bMax <= aMax:
        return 1
    else:
        return 0

def overlaps(aMin,aMax,bMin,bMax) -> int:    
    if aMin >= bMin and aMin <= bMax:
        return 1
    elif bMin >= aMin and bMin <= aMax:
        return 1
    elif aMax >= bMin and aMax <= bMax:
        return 1
    elif bMax >= aMin and bMax <= aMax:
        return 1
    else:
        return 0





#file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem4-Example.txt','r')
file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem4-Input.txt','r')

all = file.read().splitlines()
sumContains = 0
sumOverlaps = 0
for l in all:
    
    a, b = l.split(',')
    aMin, aMax = map(int, a.split('-'))
    bMin, bMax = map(int, b.split('-'))
    sumContains += contains(aMin,aMax,bMin,bMax)
    sumOverlaps += overlaps(aMin,aMax,bMin,bMax)
print(sumContains, ',', sumOverlaps)