import random
#Generate the board
#Print the board, but hide the ships
#Get user input
#Check if theres a hit
#Update the board
#Check for a win
#print the board
#go back to get input

GRID_SIZE_X = 3  #constants: do in caps
GRID_SIZE_Y = 3
NUM_SHIPS = 2  # Ships are all 1x1

# GENERATING BOARD WITH SHIPS
def gen_ship(board):  #brackets = parameters, not necesarily same 'board'as below
    x = random.randint(0,GRID_SIZE_X - 1)  # random function generates including 0 and 9 so 10th no. is 9
    y = random.randint(0,GRID_SIZE_Y - 1)
    if board[x][y] == 1:
        gen_ship(board)
    else:
        board[x][y] = 1

def gen_board():  #colon needed when line of code creates new indent
    board = []  # [] means an empty list
    for x in range(0, GRID_SIZE_X):
        board.append([]) #append means add on to end, so for every x value you add a new empty
                        #list, hence making it 2 dimensional.
        for y in range(0, GRID_SIZE_Y):
            #Put y for loop in x one (NESTED FOR LOOP) so you get a y value
            #for every x value not just a y axis of values - means loop does x=0
            #then y=0 up to 10 then does for x=1, y=0 to 10.

            board[x].append(0)

    for d in range(0, NUM_SHIPS):

        #can do it like below and not as a recursive function
        #(function that calls itself) but is less readable and easy to understand
        #--> needed to ensure the same square isnt randomly generated more than once

        #x = random.randint(0,GRID_SIZE_X - 1)
        #y = random.randint(0,GRID_SIZE_Y - 1)
        #while board[x][y] == 1:
        #    x = random.randint(0,GRID_SIZE_X - 1)
        #    y = random.randint(0,GRID_SIZE_X - 1)
        #board[x][y] = 1

        gen_ship(board)

    return board

# PRINTING BOARD
def print_line():
    for linelength in range(0, (GRID_SIZE_X * 4) + 1):
        print("-", end='')
    print("")

def print_board(board):
    print("Opponent's Board:")
    print_line()

    for y in range(0, GRID_SIZE_Y):
        print("|", end='')
        for x in range(0, GRID_SIZE_X):
            if board[x][y] == 1: #hides the ships so they also show up 0
                print(" " + str(0) + " |", end='')
            else: #if hit or miss then won't be hidden
                print(" " + str(board[x][y]) + " |", end='')
        print("")
        print_line()


'''def assessHit(board,x,y):

    if board[x][y] == 1:
        board[x][y] = str('!')
        print_board(board)
        print("Hit!")
        numberHit += 1
        return numberHit

    elif board[x][y] == 0:
        board[x][y] = str('x')
        print_board(board)
        print("Miss!")

    else:
        print("Coordinate already tried")'''

def enterCoordinates():
        attempt = input("Enter hit coordinates: ")
        return attempt

def assessCoordinate(board,count):
    coords = enterCoordinates().split(",") #splits the inputted string (coordinate) into a list defined by the comma
    if len(coords) == 2: #len=length ie. how many values in list
        print("Correct length coordinate")

        if int(coords[0]) in range(1, GRID_SIZE_X + 1) and int(coords[1]) in range(1, GRID_SIZE_Y + 1):
# range includes first number given (1) but not last number given (grid size + 1)

                x = int(coords[0]) - 1 #to make coordinates 1-10 not 0-9
                y = int(coords[1]) - 1
                if board[x][y] == 1:
                    board[x][y] = str('!')
                    print_board(board)
                    print("Hit!")
                    return True

                elif board[x][y] == 0:
                    board[x][y] = str('x')
                    print_board(board)
                    print("Miss!")

                else:
                    print("Coordinate already tried")
        else:
            print("Coordinates must be between 1 and ", GRID_SIZE_X, "- try again")
    else:
        print("Coordinate must be two numbers separated by a comma - try again")

def assessWin(board,count):
    if assessCoordinate(board,count) == True:
        count += 1
        if NUM_SHIPS - count == 1:
            print("1 boat left to hit!")
        else:
            print(NUM_SHIPS - count, " boats left to hit!")
        if count == NUM_SHIPS:
            print("You've won!")
            return #ends the function - means won't assessWin again aka game has ended
    assessWin(board,count)

def main():
    board = gen_board() #generates a board
    print_board(board) #prints that board
    assessWin(board,0) #assessWin includes assessCoordinate which includes enterCoordinates


main()
#TO DO
#if input not numbers eg. w,3
#say how many ships remaining
#make boats more than one square - after randint, next boat is one of the spaces around it
