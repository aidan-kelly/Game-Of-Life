import sys
import os
import random

size = 5
maxRow = size-1
maxCol = size-1

gameState = []

for i in range(size-1):
    gameState.append([])
    for j in range(size-1):
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


def getNeighbors(oRow, oCol):
    print(oRow)
    print(oCol)

    if oRow == 0 and oCol == 0:
        return [[0,1], [1,0], [1,1]]

    elif oRow ==0 and oCol == maxCol:
        return [[0, maxCol-1], [1, maxCol-1], [1, maxCol]]

    elif oRow == 0:
        return [[0, oCol-1], [0, oCol+1], [1, oCol-1], [1, oCol], [1, oCol+1]]

    elif oRow == maxRow and oCol == 0:
        return [[maxRow-1, 0], [maxRow-1, 1], [maxRow, 1]]

    elif oRow == maxRow and oCol == maxCol:
        return [[maxRow, oCol-1], [maxRow-1, oCol-1], [maxRow-1, oCol]]

    elif oRow == maxRow:
        return [[maxRow, oCol-1], [maxRow, oCol+1], [maxRow-1, oCol-1], [maxRow-1, oCol], [maxRow-1, oCol+1]]

    elif oCol == 0:
        return [[oRow-1, oCol], [oRow-1, oCol+1],
                [oRow, oCol+1], 
                [oRow+1, oCol], [oRow+1, oCol+1]]

    elif oCol == maxCol:
        return [[oRow-1, oCol], [oRow-1, oCol-1],
                [oRow, oCol-1],
                [oRow+1, oCol], [oRow+1, oCol-1]]


    else:

        return [[oRow-1, oCol-1], [oRow-1 , oCol], [oRow-1 , oCol+1],
                [oRow, oCol-1], [oRow, oCol+1],
                [oRow+1, oCol-1], [oRow+1, oCol], [oRow+1, oCol+1]]




def liveOrDie(neighbors, entry):

    liveNeighborCount = 0
    for neighbor in neighbors:
        print(neighbor[0])
        print(neighbor[1])
        if gameState[neighbor[0]][neighbor[1]] == 'X':
            liveNeighborCount += 1

    if(liveNeighborCount < 2 and entry == 'X'):
        return False
    elif(liveNeighborCount >3 and entry =='X'):
        return False
    elif(entry == '-' and liveNeighborCount == 3):
        return True
    else: 
        return True
    
    
    print(liveNeighborCount)

def main():

    while(True):

        global gameState
        tempGameState = gameState

        for rindex, row in enumerate(gameState):

            tempGameState.append([])
            for cindex, column in enumerate(gameState):
                ourNeighbors = getNeighbors(rindex, cindex)
                print(ourNeighbors)
                result = liveOrDie(ourNeighbors, gameState[rindex][cindex])
                
                if(result == True):
                    tempGameState[rindex].append('X')
                else:
                    tempGameState[rindex].append('-')
        
        printGameboard(tempGameState)
        gameState = tempGameState

    printGameboard(gameState)


main()