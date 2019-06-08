'''
A simple implementation of Conway's Game of Life. 
Input an integer as command line agrument to serve as the gameboard size.
Written by Aidan Kelly. 
June 8, 2019

'''

import sys
import os
import random
import time

#ensuring that we have an integer inputted.
if(len(sys.argv) != 2):
    print("Please enter the size of board you want to use as a command line argument.")
    sys.exit()

try:
    size = int(sys.argv[1])
except:
    print("Please enter an integer for the size of your board.")
    sys.exit()

#setting up our variables
maxRow = size-1
maxCol = size-1
liveToken = '0'
deadToken = ' '

#loop to build us a randomly generated gamestate
gameState = []
for i in range(size):
    gameState.append([])
    for j in range(size):
        randInt = random.randint(0,1)
        if(randInt == 0):
            gameState[i].append(deadToken)
        else:
            gameState[i].append(liveToken)


#function to print the gamestate.
def printGameboard(gameState):

    #loop through the gamestate and print the token.
    for index in gameState:
        for item in index:
            sys.stdout.write(str(item))
        print("")

    for i in range(5):
        print("")


#Function to get the indices of a index's neighbors. 
def getNeighbors(row, col):

    #returns all of the neighbors based off of the caller's positioning on the board.
    if row == 0 and col == 0:
        return [[0,1], 
                [1,0], [1,1]]

    elif row ==0 and col == maxCol:
        return [[0, maxCol-1], 
                [1, maxCol-1], [1, maxCol]]

    elif row == 0:
        return [[0, col-1], [0, col+1], 
                [1, col-1], [1, col], [1, col+1]]

    elif row == maxRow and col == 0:
        return [[maxRow-1, 0], 
                [maxRow-1, 1], [maxRow, 1]]

    elif row == maxRow and col == maxCol:
        return [[maxRow, col-1], 
                [maxRow-1, col-1], [maxRow-1, col]]

    elif row == maxRow:
        return [[maxRow, col-1], [maxRow, col+1], 
                [maxRow-1, col-1], [maxRow-1, col], [maxRow-1, col+1]]

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


#determine if a cell should live or die.
def liveOrDie(neighbors, entry):

    #first we count the cell's live neighbors. 
    liveNeighborCount = 0
    for neighbor in neighbors:
        if gameState[neighbor[0]][neighbor[1]] == liveToken:
            liveNeighborCount += 1

    #we then make the cell live or dead based off of the rules of the game. 
    if(liveNeighborCount < 2 and entry == liveToken):
        return False
    elif(liveNeighborCount >3 and entry ==liveToken):
        return False
    elif(entry == deadToken and liveNeighborCount == 3):
        return True
    elif(entry == liveToken and (liveNeighborCount == 2 or liveNeighborCount ==3)):
        return True
    else: 
        return False
    

#main function to start the gameloop
def main():

    #infinitly loop the game. 
    while(True):

        global gameState
        tempGameState = []

        #loop through all indicies. 
        for i in range(0,size):

            #add a row to our temp gamestate. 
            tempGameState.append([])

            #loop through the columns. 
            for j in range(0,size):

                #find our neighbors
                ourNeighbors = getNeighbors(i, j)

                #based off of our neighbors, make our cell live or dead
                result = liveOrDie(ourNeighbors, gameState[i][j])
                
                #update our cell
                if(result == True):
                    tempGameState[i].append(liveToken)
                else:
                    tempGameState[i].append(deadToken)
        
        #print out the gameboard
        printGameboard(tempGameState)

        #make our temp gamestate the new gamestate
        gameState = tempGameState

        #sleep half a second so that the user can see what is happening. 
        time.sleep(0.5)

main()