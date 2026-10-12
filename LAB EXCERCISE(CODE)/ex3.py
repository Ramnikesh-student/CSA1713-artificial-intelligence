from collections import deque

# Function to solve the Water Jug Problem
def water_jug(jug1, jug2, target):

    # Queue stores the current amount of water
    # in Jug 1 and Jug 2
    queue = deque()

    # Start with both jugs empty
    queue.append((0, 0))

    # Store visited states
    visited = set()

    while queue:

        # Get current state
        a, b = queue.popleft()

        # If this state was already visited, skip it
        if (a, b) in visited:
            continue

        visited.add((a, b))

        print("Jug 1:", a, "Jug 2:", b)

        # Check whether target is reached
        if a == target or b == target:
            print("Target reached!")
            return

        # 1. Fill Jug 1
        queue.append((jug1, b))

        # 2. Fill Jug 2
        queue.append((a, jug2))

        # 3. Empty Jug 1
        queue.append((0, b))

        # 4. Empty Jug 2
        queue.append((a, 0))

        # 5. Pour Jug 1 into Jug 2
        amount = min(a, jug2 - b)
        queue.append((a - amount, b + amount))

        # 6. Pour Jug 2 into Jug 1
        amount = min(b, jug1 - a)
        queue.append((a + amount, b - amount))


# Main program

jug1 = 4
jug2 = 3
target = 2

print("Water Jug Problem")
print("-----------------")

water_jug(jug1, jug2, target)
