#Defining the global variables
board=[
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
        ]

currentPlayer = "X"
winner= None
gameRunning = True

#Print the game board
def printGame(board):
    print("*********")
   
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")

    print(board[6] + " | " + board[7] + " | " + board[8])
    print("*********")

# printGame(board)

#Take player input
def playerInput(board):
    
    print("---------------------------------------------")
    inp = int(input("Enter any number from 0 to 9: "))
    print("---------------------------------------------")

    if inp>=0 and inp<=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("---------------------------------------------")
        print("Ooops! Board contains player, try again")

#Check for win or tie
def checkHorizontal(board): #check horizontal
    global winner
    if board[0]== board[2] == board[3] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3]== board[4]== board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6]== board[7]== board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRows(board): #check vertically

    global winner

    if board[0]== board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1]== board[4]== board[7] and board[1] != "-":
        winner = board[1]
        return True

    elif board[2]== board[5]== board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board): #check diagonally
    global winner

    if board[0]== board[8] == board[9] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2]== board[4]== board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board): #check for a tie
    global gameRunning
    if "-" not in board:
        printGame(board)
        print("It's a tie")
        gameRunning = False

#Check for a winner

def checkWin():
    if checkDiagonal(board) or checkRows(board) or checkHorizontal(board):
        print(f"The winner is {winner}")

#Switch the player
def switchPlayer(): #Switch between players
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#Check for win or tie again

while gameRunning:
    printGame(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
