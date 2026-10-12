# Missionaries and Cannibals Problem
from collections import deque
# Check whether the situation is safe
def safe(m_left, c_left):
    # Number on the right side
    m_right = 3 - m_left
    c_right = 3 - c_left
    # Check left side
    if m_left > 0 and c_left > m_left:
        return False
    # Check right side
    if m_right > 0 and c_right > m_right:
        return False
    return True
# Solve the problem
def solve():
    # Starting state
    # (Missionaries, Cannibals, Boat)
    start = (3, 3, "Left")
    # Goal state
    goal = (0, 0, "Right")
    # Queue
    queue = deque()
    queue.append((start, [start]))
    # Visited states
    visited = set()
    visited.add(start)
    # Possible boat movements
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]
    while queue:
        state, path = queue.popleft()
        m_left = state[0]
        c_left = state[1]
        boat = state[2]
        # Check whether everyone crossed
        if state == goal:
            return path
        # Try every possible boat movement
        for m, c in moves:
            if boat == "Left":
                # Move from left to right
                new_m = m_left - m
                new_c = c_left - c
                new_boat = "Right"
            else:
                # Move from right to left
                new_m = m_left + m
                new_c = c_left + c
                new_boat = "Left"
            # Check valid number of people
            if new_m < 0 or new_c < 0:
                continue
            if new_m > 3 or new_c > 3:
                continue
            # Check whether state is safe
            if safe(new_m, new_c):
                new_state = (new_m, new_c, new_boat)
                # Check if already visited
                if new_state not in visited:
                    visited.add(new_state)
                    new_path = path + [new_state]
                    queue.append((new_state, new_path))
    return None
# Run the program
answer = solve()
# Display the answer
if answer:
    print("Solution Found!")
    print()
    for state in answer:
        print(state)
else:
    print("No solution")
