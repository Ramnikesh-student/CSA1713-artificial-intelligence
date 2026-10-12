# Crypt-Arithmetic Problem
# SEND + MORE = MONEY

from itertools import permutations

# Letters used in the problem
letters = "SENDMORY"

# Try different digits
for values in permutations(range(10), 8):

    S = values[0]
    E = values[1]
    N = values[2]
    D = values[3]
    M = values[4]
    O = values[5]
    R = values[6]
    Y = values[7]

    # S and M cannot be zero
    if S == 0 or M == 0:
        continue

    # Make the numbers
    SEND = S * 1000 + E * 100 + N * 10 + D
    MORE = M * 1000 + O * 100 + R * 10 + E
    MONEY = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

    # Check the answer
    if SEND + MORE == MONEY:

        print("Solution Found!")
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)

        break
