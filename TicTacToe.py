# Setup
board = [str(i) for i in range(10)]
currentPlayer = 'X'
gameOver = False

# Function to display the board
def printBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print()

# Function to check if board is full
def boardIsFull(board):
    for i in range(1, 10):
        if board[i] != 'X' and board[i] != 'O':
            return False
    return True