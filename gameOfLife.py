import sys
import os
import random
import time

if(len(sys.argv) != 2):
    print("Please enter the size of board you want to use as a command line argument.")
    sys.exit()

try:
    size = int(sys.argv[1])
except:
    print("Please enter an integer for the size of your board.")
    sys.exit()

maxRow = size-1
maxCol = size-1

gameState = []

for i in range(size):
    gameState.append([])
    for j in range(size):
        randInt = random.randint(0,1)
        if(randInt == 0):
            gameState[i].append('-')
        else:
            gameState[i].append('X')

def printGameboard(gameState):
    for index in gameState:
        for item in index:
            sys.stdout.write(str(item))
        print("")

    for i in range(5):
        print("")


def getNeighbors(row, col):

    if row == 0 and col == 0:
        return [[0,1], [1,0], [1,1]]

    elif row ==0 and col == maxCol:
        return [[0, maxCol-1], [1, maxCol-1], [1, maxCol]]

    elif row == 0:
        return [[0, col-1], [0, col+1], [1, col-1], [1, col], [1, col+1]]

    elif row == maxRow and col == 0:
        return [[maxRow-1, 0], [maxRow-1, 1], [maxRow, 1]]

    elif row == maxRow and col == maxCol:
        return [[maxRow, col-1], [maxRow-1, col-1], [maxRow-1, col]]

    elif row == maxRow:
        return [[maxRow, col-1], [maxRow, col+1], [maxRow-1, col-1], [maxRow-1, col], [maxRow-1, col+1]]

    elif col == 0:
        return [[row-1, col], [row-1, col+1],
                [row, col+1], 
                [row+1, col], [row+1, col+1]]

    elif col == maxCol:
        return [[row-1, col], [row-1, col-1],
                [row, col-1],
                [row+1, col], [row+1, col-1]]


    else:

        return [[row-1, col-1], [row-1 , col], [row-1 , col+1],
                [row, col-1], [row, col+1],
                [row+1, col-1], [row+1, col], [row+1, col+1]]




def liveOrDie(neighbors, entry):

    liveNeighborCount = 0
    for neighbor in neighbors:
        if gameState[neighbor[0]][neighbor[1]] == 'X':
            liveNeighborCount += 1

    if(liveNeighborCount < 2 and entry == 'X'):
        return False
    elif(liveNeighborCount >3 and entry =='X'):
        return False
    elif(entry == '-' and liveNeighborCount == 3):
        return True
    elif(entry == "X" and (liveNeighborCount == 2 or liveNeighborCount ==3)):
        return True
    else: 
        return False
    

def main():

    counter=0
    while(True):

        global gameState
        tempGameState = []

        for i in range(0,size):
            tempGameState.append([])
            for j in range(0,size):

                ourNeighbors = getNeighbors(i, j)
                result = liveOrDie(ourNeighbors, gameState[i][j])
                
                if(result == True):
                    tempGameState[i].append('X')
                else:
                    tempGameState[i].append('-')
        
        printGameboard(tempGameState)
        gameState = tempGameState
        counter+=1

        time.sleep(0.5)



main()