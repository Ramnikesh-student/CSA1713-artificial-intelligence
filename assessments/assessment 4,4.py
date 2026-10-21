
# Minimax Algorithm

def minimax(node, maximizing):
    if isinstance(node, int):
        return node

    values = [minimax(child, not maximizing) for child in node]

    if maximizing:
        return max(values)
    return min(values)

tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

print("Minimax value:", minimax(tree, True))

# Tic-tac-toe evaluation
board = [
    ['X', 'O', ' '],
    [' ', 'X', ' '],
    [' ', ' ', 'O']
]

lines = []

for row in board:
    lines.append(row)

for col in range(3):
    lines.append([board[row][col] for row in range(3)])

lines.append([board[i][i] for i in range(3)])
lines.append([board[i][2-i] for i in range(3)])

open_x = sum('O' not in line for line in lines)
open_o = sum('X' not in line for line in lines)

print("Open lines for X:", open_x)
print("Open lines for O:", open_o)
print("Evaluation E:", open_x - open_o)
