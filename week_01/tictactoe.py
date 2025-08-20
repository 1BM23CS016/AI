def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    """Gets a valid move from the player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_system_move(board):
    """Determines the system's move (basic AI)."""
    # 1. Check for a winning move for the system
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                if check_win(board, "O"):
                    return r, c
                board[r][c] = " "  # Undo the move
    
    # 2. Check to block the player's winning move
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "X"
                if check_win(board, "X"):
                    board[r][c] = " " # Undo the move
                    return r, c
                board[r][c] = " " # Undo the move
    
    # 3. Take the center if available
    if board[1][1] == " ":
        return 1, 1

    # 4. Take a corner if available
    corners = [(0,0), (0,2), (2,0), (2,2)]
    for r, c in corners:
        if board[r][c] == " ":
            return r, c

    # 5. Take any available side
    sides = [(0,1), (1,0), (1,2), (2,1)]
    for r, c in sides:
        if board[r][c] == " ":
            return r, c

def play_game():
    """Manages the Tic-Tac-Toe game flow."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Player is 'X', System is 'O'

    while True:
        print_board(board)
        if current_player == "X":
            row, col = get_player_move(board)
        else:
            print("System's turn...")
            row, col = get_system_move(board)

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
