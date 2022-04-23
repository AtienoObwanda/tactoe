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
