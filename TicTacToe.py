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

# Function to chose X or O
def chooseMarkers():

    while True:
        choice = input("Player 1, Choose your marker (X/O): ").strip().upper()
        if choice in ("X", "O"):
            return (choice, "O" if choice == "X" else "X")
        print("Invalid choice. Please choose X or O.")

# Function to check if input is valid
def isValidMove(choice):
    try:
        pos = int(choice)
    except (TypeError, ValueError):
        return False
    return 1 <= pos <= 9

# FUnction to check if board position is taken
def isTaken(board, choice):
    return board[choice] in ('X', 'O')

# Function for Player Move
def getPlayerMove(board, currentPlayer):
    while True:
        raw = input(f"{currentPlayer}, enter your move (1-9): ").strip()
        if not isValidMove(raw):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        pos = int(raw)
        if isTaken(board, pos):
            print("Position already taken. Choose another.")
            continue
        return pos
    
    