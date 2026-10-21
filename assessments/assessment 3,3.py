
# Minimax Algorithm

def minimax(scores, depth, maximizing):
    if depth == 2:
        return scores.pop(0)

    if maximizing:
        return max(
            minimax(scores, depth + 1, False),
            minimax(scores, depth + 1, False)
        )
    else:
        return min(
            minimax(scores, depth + 1, True),
            minimax(scores, depth + 1, True)
        )

def evaluate_pair(a, b):
    return max(a, b)

# X's final choices for each O reply
reply_values = [
    evaluate_pair(4, 7),
    evaluate_pair(8, 2),
    evaluate_pair(3, 5),
    evaluate_pair(6, 9)
]

move1 = min(reply_values[0], reply_values[1])
move2 = min(reply_values[2], reply_values[3])
best_score = max(move1, move2)

print("Values of O's replies:", reply_values)
print("Value of X's first move 1:", move1)
print("Value of X's first move 2:", move2)
print("Best guaranteed score:", best_score)
print("Best first move: Move 1")
