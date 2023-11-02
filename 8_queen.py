def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_queens_util(board, row):
    if row == len(board):
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            
            if solve_queens_util(board, row + 1):
                return True
            
            board[row][col] = 0
    
    return False

def solve_queens():
    n = 8  # Change this value to solve for different board sizes
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_queens_util(board, 0):
        return board
    else:
        return None

def print_board(board):
    for row in board:
        print(' '.join(['Q' if col == 1 else '.' for col in row]))

# Example usage:
solution = solve_queens()

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution exists.")
