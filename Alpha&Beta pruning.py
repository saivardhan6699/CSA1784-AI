import math

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: If we reach a leaf node
    if depth == 3:  # Assuming a depth of 3 for this example
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Each node has two children
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Running Alpha-Beta Pruning from the root (depth = 0, node_index = 0)
optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
print("Optimal value: ", optimal_value)
