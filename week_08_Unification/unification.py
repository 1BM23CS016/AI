 
import math

def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def evaluate(board, n):
    """Heuristic: number of non-attacking pairs (the higher, the better)."""
    safe_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != -1 and board[j] != -1 and abs(board[i] - board[j]) != abs(i - j) and board[i] != board[j]:
                safe_pairs += 1
    return safe_pairs


def minimax(board, depth, n, is_max, alpha, beta):
    """Minimax with Alpha-Beta pruning for N-Queens."""
    if depth == n:
        return evaluate(board, n), board

    if is_max:
        max_eval = -math.inf
        best_board = None
        for col in range(n):
            if is_safe(board, depth, col):
                board[depth] = col
                eval_val, _ = minimax(board[:], depth + 1, n, False, alpha, beta)
                if eval_val > max_eval:
                    max_eval = eval_val
                    best_board = board[:]
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break  # Alpha-beta pruning
        return max_eval, best_board

    else:
        # "Min" tries to minimize safety (simulate adversarial conflict)
        min_eval = math.inf
        worst_board = None
        for col in range(n):
            if is_safe(board, depth, col):
                board[depth] = col
                eval_val, _ = minimax(board[:], depth + 1, n, True, alpha, beta)
                if eval_val < min_eval:
                    min_eval = eval_val
                    worst_board = board[:]
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break
        return min_eval, worst_board


def solve_n_queens(n):
    """Wrapper to find a configuration using minimax + alpha-beta."""
    board = [-1] * n
    score, final_board = minimax(board, 0, n, True, -math.inf, math.inf)
    return final_board


# Run example
if __name__ == "__main__":
    n = 8
    solution = solve_n_queens(n)
    print("Solution board (row -> column):", solution)
    
    # Visualize board
    for r in range(n):
        row = ['Q' if solution[r] == c else '.' for c in range(n)]
        print(' '.join(row))
