

def problem2partb(list):
    playerA = 'ABC' #0 1 2
    playerB = 'XYZ' #0 1 2

    totalscore = 0

    for l in all:
        A, B = l.split() 
        locA = playerA.index(A)
        locB = playerB.index(B)
        
        if locB == 0: #loose
            if locA == 0:    
                score = 3
            else:
                score = locA 
        elif locB == 1: #even
            score = locA + 4
        elif locB == 2:
            if locA == 2:
                score = 7
            else: #win
                score = locA + 8
        totalscore += score
        
    print(totalscore)


def problem2parta(list):
    playerA = 'ABC' #0 1 2
    playerB = 'XYZ' #0 1 2

    totalscore = 0

    for l in all:        
        A, B = l.split() 
        locA = playerA.index(A)
        locB = playerB.index(B)
        
        if locA == locB:
            score =  locB + 4 # 3 for Draw + 1 for index         
        elif locB -2 == locA:
            score =  locB + 1  # 1 for index (my Scissors vs. rock)        
        elif locA -2 == locB:
            score =  locB + 7   # 6 for win + 1 for index (my rock vs. scissors)
        elif locB > locA:
            score =  locB + 7  # 6 for win + 1 for index
        else:
            score =  locB + 1 # 1 for loss        
        totalscore +=  score
    print(totalscore)


#file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem2-Example.txt','r')
file = open('C:\Forritun\PythonStuff\AdventOfCode2022\Input\Problem2-Input.txt','r')


all = file.read().splitlines()
#print(all)

problem2parta(all)
problem2partb(all)


    #11939 too low