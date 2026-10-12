from collections import deque

# Goal state
goal = "123456780"


# Function to print the puzzle
def print_puzzle(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


# Function to find possible moves
def get_moves(state):

    moves = []

    # Find the blank space (0)
    blank = state.index("0")

    # Move Up
    if blank >= 3:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]

        moves.append("".join(new_state))

    # Move Down
    if blank <= 5:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]

        moves.append("".join(new_state))

    # Move Left
    if blank % 3 != 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]

        moves.append("".join(new_state))

    # Move Right
    if blank % 3 != 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]

        moves.append("".join(new_state))

    return moves


# BFS function
def solve_puzzle(start):

    queue = deque()

    # Store the starting state
    queue.append([start])

    # Store already visited states
    visited = set()
    visited.add(start)

    while queue:

        # Get the first path
        path = queue.popleft()

        # Get the current state
        current = path[-1]

        # Check if goal is reached
        if current == goal:
            return path

        # Get all possible moves
        next_states = get_moves(current)

        for next_state in next_states:

            # If state is not visited
            if next_state not in visited:

                visited.add(next_state)

                # Create a new path
                new_path = path + [next_state]

                # Add it to the queue
                queue.append(new_path)

    return None


# Main program

# Initial state
start = "123406758"

print("Initial Puzzle:")
print_puzzle(start)

# Solve the puzzle
solution = solve_puzzle(start)

# Display solution
if solution is not None:

    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for i in range(len(solution)):

        print("Step", i)
        print_puzzle(solution[i])

else:

    print("No solution exists.")
