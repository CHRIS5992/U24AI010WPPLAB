def solve_queens():
    def is_safe(board, row, col):
        # Check column and diagonals for conflicts
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == row - i:
                return False
        return True

    def backtrack(row, board, results):
        if row == 8:  # All queens placed successfully
            results.append(board[:])
            return
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board, results)

    results = []
    backtrack(0, [0] * 8, results)
    return results

# Get all valid solutions
solutions = solve_queens()
print(f"Total solutions: {len(solutions)}")
print("Sample solution:")
print(solutions[0])  # Print the first solution