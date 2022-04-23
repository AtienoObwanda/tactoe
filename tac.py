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

printGame(board)

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

