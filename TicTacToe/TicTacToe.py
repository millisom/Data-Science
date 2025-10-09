# Setup
board = [str(i) for i in range(10)]
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

# Function to check if board position is taken


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

# Function to check for a winner


def checkWinner(board, mark):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == mark for i in combo):
            return True
    return False

# Main Game Loop


def playGame():
    board = [str(i) for i in range(10)]
    gameOver = False
    print("Welcome to Tic Tac Toe!")
    player1Marker, player2Marker = chooseMarkers()
    currentPlayer, currentMarker = "Player 1", player1Marker
    printBoard(board)
    while not gameOver:
        move = getPlayerMove(board, currentPlayer)
        board[move] = currentMarker
        printBoard(board)
        if checkWinner(board, currentMarker):
            print(f"Congratulations {currentPlayer}! You have won the game!")
            gameOver = True
        elif boardIsFull(board):
            print("The game is a draw!")
            gameOver = True
        else:
            currentPlayer, currentMarker = (
                "Player 2", player2Marker) if currentPlayer == "Player 1" else ("Player 1", player1Marker)


# Start the game
if __name__ == "__main__":
    while True:
        playGame()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break
