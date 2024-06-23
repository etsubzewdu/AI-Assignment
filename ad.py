def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winner = None

    while not winner and not is_full(board):
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        
        while True:
            try:
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))
                if row in range(3) and col in range(3) and board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number.")

        winner = check_winner(board)
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if name == "main":
    play_game()