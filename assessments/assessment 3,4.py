
# Alpha-Beta Pruning

def alpha_beta(moves):
    alpha = float('-inf')
    best_move = None
    evaluated = 0

    for name, scores in moves:
        beta = float('inf')
        value = float('inf')

        for score in scores:
            evaluated += 1
            value = min(value, score)
            beta = min(beta, value)

            if beta <= alpha:
                print(name, "- pruning remaining scores")
                break

        print(name, "value:", value)

        if value > alpha:
            alpha = value
            best_move = name

    print("Positions evaluated:", evaluated)
    print("Positions pruned:", 9 - evaluated)
    print("Best move:", best_move)
    print("Best value:", alpha)

moves = [
    ("M1", [6, 9, 7]),
    ("M2", [4, 8, 10]),
    ("M3", [7, 5, 12])
]

alpha_beta(moves)
