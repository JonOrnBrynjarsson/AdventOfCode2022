
#file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem1a-Example.txt','r')
from operator import truediv


file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem1a-Input.txt','r')

all = file.read().splitlines()

currCal = 0
listCal = []

for l in all:
    if l != '' :
        currCal = currCal + int(l)
    else:
        listCal.append(currCal)
        currCal = 0

listCal.append
listCal.sort(reverse=True)

AnsA = listCal[0]
AnsB =sum(listCal[0:3])

print(AnsA, AnsB )

