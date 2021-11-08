from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|       "*3,"|",sep="")
        for column in range(3):
            print("|   "+str(board[row][column]),"   ",sep="",end="")
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")
        
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    status = False 
    while not status :
        move = input("Enter your move: ")
        status = (len(move) == 1) and (not(int(move) <=0)) and (not(int(move) > 9))
        if  not status :
            print("Your input is incorrect, try again")
            continue
        move = int(move)-1
        row = move // 3 
        column =  move % 3
        status = board[row][column] not in  ["X","O"]
        if not status:
            print("Field already use or occupied")
            continue
        board[row][column]= "O"
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X","O"]:
                free_squares.append((row,column))
    return free_squares
                

def victory_for(board, sgn):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sgn == "X":
        who = "computer"	
    elif sgn == "O": 
        who = 'you'	
    else:
        who = None	
    cross1 = cross2 = True  #check for diagonals
    for rc in range(3): # rc variable use for the browse of board
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn: 
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: 
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_field = make_list_of_free_fields(board)
    cnt = len(free_field)
    #print(cnt)
    if cnt > 0:
        random_play = randrange(cnt)
        row, col = free_field[random_play]
        board[row][col] = 'X'
    
    
#Execution of program
Board = [[3*i+j+1 for j in range(3)] for i in range(3)]
Board[1][1]="X"
#display_board(Board)
free_field = make_list_of_free_fields(Board)
human = True 
while len(free_field):
	display_board(Board)
	if human:
		enter_move(Board)
		victory = victory_for(Board,'O')
	else:	
		draw_move(Board)
		victory = victory_for(Board,'X')
	if victory != None:
		break
	human = not human		
	free = make_list_of_free_fields(Board)

display_board(Board)

if victory == 'you':
	print("You won!")
elif victory == "computer":
	print("I won")
else:
	print("Tie!")
