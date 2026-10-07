from collections import deque

# 5 x 5 grid
# Blocked cells
blocked = {(2, 2), (2, 3), (3, 3), (4, 2), (4, 4)}

start = (1, 1)
goal = (5, 5)

# Movement order: Up, Down, Left, Right
moves = [
    (-1, 0),   # Up
    (1, 0),    # Down
    (0, -1),   # Left
    (0, 1)     # Right
]


# Check whether a cell is valid
def is_valid(cell):
    row, col = cell

    if row < 1 or row > 5:
        return False

    if col < 1 or col > 5:
        return False

    if cell in blocked:
        return False

    return True


# Find neighboring cells
def get_neighbors(cell):
    row, col = cell
    neighbors = []

    for dr, dc in moves:
        new_cell = (row + dr, col + dc)

        if is_valid(new_cell):
            neighbors.append(new_cell)

    return neighbors


# ---------------- BFS ----------------

def bfs():
    queue = deque()

    # Store cell and path
    queue.append((start, [start]))

    visited = {start}

    while queue:

        current, path = queue.popleft()

        # Check goal
        if current == goal:
            return path

        # Generate neighbors
        for next_cell in get_neighbors(current):

            if next_cell not in visited:

                visited.add(next_cell)

                new_path = path + [next_cell]

                queue.append((next_cell, new_path))

    return None


# ---------------- DFS ----------------

def dfs():
    stack = []

    # Store cell and path
    stack.append((start, [start]))

    visited = {start}

    while stack:

        current, path = stack.pop()

        # Check goal
        if current == goal:
            return path

        # Add neighboring cells
        for next_cell in get_neighbors(current):

            if next_cell not in visited:

                visited.add(next_cell)

                new_path = path + [next_cell]

                stack.append((next_cell, new_path))

    return None


# Run BFS
bfs_path = bfs()

print("BFS Path:")
print(bfs_path)

print("BFS Cost:")
print(len(bfs_path) - 1)


# Run DFS
dfs_path = dfs()

print("\nDFS Path:")
print(dfs_path)

print("DFS Cost:")
print(len(dfs_path) - 1)
