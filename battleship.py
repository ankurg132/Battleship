import random

# class for ship structure and behaviour
class Ship:
    ship_position = []
    def __init__(self, size_of_ship=3, grid_size=(5, 5)):
        #initialisation of the variables of the object ship
        self.size_of_ship = size_of_ship
        self.grid_size = grid_size
        orientation = random.choice([True, False])                                                          #True for vertical orientation; False for horizontal orientation
        if orientation:
            ship_start_row = random.randrange(0, (grid_size[0] - size_of_ship + 1))        #chooses a point randomly between 0 to 3(default) so that the ship stays on the board
            ship_start_col = random.randrange(0, grid_size[1])                           #chooses a point randomly between 0 to 5(default)
            for i in range(0, size_of_ship):
                self.ship_position.append([ship_start_row + i, ship_start_col])                                  #assigns three consecutive cordinates to the ship
        else:
            ship_start_col = random.randrange(0, (grid_size[1] - size_of_ship + 1))       #chooses a point randomly between 0 to 3(default) so that the ship stays on the board
            ship_start_row = random.randrange(0, grid_size[0])                          #chooses a point randomly between 0 to 5(default)
            for i in range(0, size_of_ship):
                self.ship_position.append([ship_start_row, ship_start_col + i])                                   #assigns three consecutive cordinates to the ship

    def check_user_guess(self, user_guess):                                                                    #function to check the guess entered by the user
        flag = False                                                                                        #flag = true (for match found), false (for match not found)
        for cord in self.ship_position:                                                                      #iterate through every cordinate to find a match for user guess
            if cord == user_guess:
                flag = True
                self.ship_position.remove(user_guess)                                                         #removes the hit cordinate from ship's cordinates
                break
        if flag:
            if self.ship_position == []:                                                                     #checks whether the ship position List is empty or not, empty for Ship's sinking
                return "Kill"
            else:
                return "Hit"
        else:
            return "Miss"

def create_board(grid_size=(5, 5)):                                                                          #function for creating board of grid_size
    board = []
    for _ in range(0, grid_size[0]):                                                                       #loop to join multiple rows of board
        row = []
        for _ in range(0, grid_size[1]):                                                                   #loop to create single row of a board
            row.append('-')
        board.append(row)
    return board                                                                                            #return created board

def show_board(board):                                                                                       #function to show the current board
    for row in board:                                                                                       #cycling through Rows
        for element in row:                                                                                 #cycling through Elements
            print(element, end=' ')
        print(" ")

def play(user_name, grid_size, ship_to_kill, board):                                                            #function for gameplay
    number_of_missiles = 0
    while True:                                                                                             #loop for taking user_guess... runs until ship sinks
        show_board(board)                                                                                    #show board before each turn
        while True:                                                                                         #loop until the user enters a valid guess
            user_guess_raw = input("Where should we Fire Capt.%s (row,column): "%user_name)                    #takes input in string form
            number_of_missiles += 1
            if user_guess_raw.isalpha():
                print("Enter number captain")
            else:
                user_guess_formatted = [(int(guess)-1) for guess in user_guess_raw.split(',')]                  #converts string type cordinates into a List with cordinates in int type
                if not len(user_guess_formatted) == 2:                                                        #condition to check whether the user inputted two cordinates
                    print("Captain please enter two cordinates")
                elif user_guess_formatted[0] < 0:                                                             #Conditions for checking whether the guess is on borad
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%user_name)
                    number_of_missiles -= 1
                elif user_guess_formatted[1] < 0:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%user_name)
                    number_of_missiles -= 1
                elif user_guess_formatted[0] > grid_size[0]:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%user_name)
                    number_of_missiles -= 1
                elif user_guess_formatted[1] > grid_size[1]:
                    print("Sorry Capt.%s, we can't fire there, it is out of the Ocean"%user_name)
                    number_of_missiles -= 1
                else:                                                                                       #Breaks out of loop when input is valid
                    print("Missile has been Fired")
                    break
        check_result = ship_to_kill.check_user_guess(user_guess_formatted)                                         #calls check_result to see whether the missile hit or not
        if check_result == "Miss":                                                                           #condition for missing the ship
            board[user_guess_formatted[0]][user_guess_formatted[1]] = 'O'
            print("We missed those pirates cap'n")
        else:                                                                                               #condition for missile htting the ship
            print("We hit 'em bad cap'n", end=" ")
            if check_result == "Kill":                                                                       #if the ship sank
                board[user_guess_formatted[0]][user_guess_formatted[1]] = 'X'
                print("and killed those one eyed tramps with %s missiles"%number_of_missiles)
                break
            else:                                                                                           #if the ship stays even after the missile hits
                board[user_guess_formatted[0]][user_guess_formatted[1]] = 'X'
                print("")
    show_board(board)                                                                                        #Showing board after the game ends

#setting up the game

GRID_SIZE = [5, 5]
NEW_SHIP = Ship()
BOARD = create_board(GRID_SIZE)

#starting game...

USER_NAME = input("Enter your name Captain: ")
play(USER_NAME, GRID_SIZE, NEW_SHIP, BOARD)                                                                    #start the game by calling function play()
