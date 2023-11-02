def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return divmod(move, 3)
        except ValueError:
            pass
        print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row, col = get_move()

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. That cell is already occupied.")

if __name__ == "__main__":
    play_game()
