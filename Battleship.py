import random

# class for ship structure and behaviour
class ship:
    shipPosition = []
    def __init__(self, sizeOfShip = 3, gridSize = [5,5]):                                                   #initialisation of the variables of the object ship
        self.sizeOfShip = sizeOfShip
        self.gridSize = gridSize
        orientation = random.choice([True, False])                                                          #True for vertical orientation; False for horizontal orientation
        if orientation:
            shipStartRow = random.choice([cord for cord in range(0,(gridSize[0] - sizeOfShip + 1))])        #chooses a point randomly between 0 to 3(default) so that the ship stays on the board
            shipStartCol = random.choice([cord for cord in range(0,gridSize[1])])                           #chooses a point randomly between 0 to 5(default)
            for i in range(0,sizeOfShip):
                self.shipPosition.append([shipStartRow + i, shipStartCol])                                  #assigns three consecutive cordinates to the ship
        else:
            shipStartCol = random.choice([cord for cord in range(0,(gridSize[1] - sizeOfShip + 1))])        #chooses a point randomly between 0 to 3(default) so that the ship stays on the board
            shipStartRow = random.choice([cord for cord in range(0,gridSize[0])])                           #chooses a point randomly between 0 to 5(default)
            for i in range(0,sizeOfShip):
                self.shipPosition.append([shipStartRow,shipStartCol + i])                                   #assigns three consecutive cordinates to the ship

    def checkUserGuess(self, userGuess):                                                                    #function to check the guess entered by the user
        flag = False                                                                                        #flag = true (for match found), false (for match not found)
        for cord in self.shipPosition:                                                                      #iterate through every cordinate to find a match for user guess
            if cord == userGuess:
                flag = True                                                                                 
                self.shipPosition.remove(userGuess)                                                         #removes the hit cordinate from ship's cordinates
                break
        if flag:
            if self.shipPosition == []:                                                                     #checks whether the ship position List is empty or not, empty for Ship's sinking
                return "Kill"
            else:
                return "Hit"
        else:
            return "Miss"

def createBoard(gridSize = [5,5]):                                                                          #function for creating board of gridsize
    board = []  
    for Row in range(0, gridSize[0]):                                                                       #loop to join multiple rows of board
        row = []
        for Col in range(0, gridSize[1]):                                                                   #loop to create single row of a board
            row.append('-')
        board.append(row)
    return board                                                                                            #return created board

def showBoard(board):                                                                                       #function to show the current board
    for row in board:                                                                                       #cycling through Rows
        for element in row:                                                                                 #cycling through Elements
            print(element, end = ' ')
        print(" ")

def play(userName, gridSize, shipToKill, board):                                                            #function for gameplay
    numberOfMissiles = 0
    while True:                                                                                             #loop for taking userguess... runs until ship sinks
        showBoard(board)                                                                                    #show board before each turn
        while True:                                                                                         #loop until the user enters a valid guess
            userGuessRaw = input("Where should we Fire Capt.%s (row,column): "%userName)                    #takes input in string form
            numberOfMissiles += 1
            if userGuessRaw.isalpha():
                print("Enter number captain")
            else:
                userGuessFormatted = [(int(guess)-1) for guess in userGuessRaw.split(',')]                  #converts string type cordinates into a List with cordinates in int type
                if not len(userGuessFormatted) == 2:                                                        #condition to check whether the user inputted two cordinates
                    print("Captain please enter two cordinates")
                elif userGuessFormatted[0] < 0:                                                             #Conditions for checking whether the guess is on borad
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%userName)
                    numberOfMissiles -= 1
                elif userGuessFormatted[1] <  0:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%userName)
                    numberOfMissiles -= 1
                elif userGuessFormatted[0] >  gridSize[0]:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%userName)
                    numberOfMissiles -= 1
                elif userGuessFormatted[1] >  gridSize[1]:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%userName)
                    numberOfMissiles -= 1
                else:                                                                                       #Breaks out of loop when input is valid
                    print("Missile has been Fired")
                    break
        checkResult = shipToKill.checkUserGuess(userGuessFormatted)                                         #calls checkResult to see whether the missile hit or not
        if checkResult == "Miss":                                                                           #condition for missing the ship
            board[userGuessFormatted[0]][userGuessFormatted[1]] = 'O'
            print("We missed those pirates cap'n")
        else:                                                                                               #condition for missile htting the ship
            print("We hit 'em bad cap'n", end = " ")
            if checkResult == "Kill":                                                                       #if the ship sank
                board[userGuessFormatted[0]][userGuessFormatted[1]] = 'X' 
                print("and killed those one eyed tramps with %s missiles"%numberOfMissiles)
                break
            else:                                                                                           #if the ship stays even after the missile hits
                board[userGuessFormatted[0]][userGuessFormatted[1]] = 'X'
                print("")
    showBoard(board)                                                                                        #Showing board after the game ends
        
#setting up the game
        
gridSize = [5,5]
newShip = ship()
board = createBoard(gridSize)

#starting game...

userName = input("Enter your name Captain: ")
play(userName, gridSize, newShip, board)                                                                    #start the game by calling function play()
