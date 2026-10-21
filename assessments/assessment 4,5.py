
# Alpha-Beta Pruning

tree = [
    [
        [[8, 6], [5, 7]],
        [[2, 9], [4, 3]]
    ],
    [
        [[6, 1], [5, 2]],
        [[9, 7], [3, 4]]
    ]
]

evaluated = 0

def alpha_beta(node, depth, alpha, beta):
    global evaluated

    if isinstance(node, int):
        evaluated += 1
        return node

    if depth % 2 == 0:  # MAX node
        value = float('-inf')

        for i, child in enumerate(node):
            value = max(
                value,
                alpha_beta(child, depth + 1, alpha, beta)
            )
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned remaining child branches at MAX")
                break

        return value

    else:  # MIN node
        value = float('inf')

        for i, child in enumerate(node):
            value = min(
                value,
                alpha_beta(child, depth + 1, alpha, beta)
            )
            beta = min(beta, value)

            if alpha >= beta:
                print("Pruned remaining child branches at MIN")
                break

        return value

result = alpha_beta(tree, 0, float('-inf'), float('inf'))

print("Root value:", result)
print("Leaves evaluated:", evaluated)
print("Leaves pruned:", 16 - evaluated)
