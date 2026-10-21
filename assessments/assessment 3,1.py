
import heapq

graph = {
    "Gate": [("Library", 120), ("Canteen", 200)],
    "Library": [("Gate", 120), ("Lab", 150), ("Hostel", 300)],
    "Canteen": [("Gate", 200), ("Hostel", 100), ("Admin", 260)],
    "Lab": [("Library", 150), ("Auditorium", 350)],
    "Hostel": [("Library", 300), ("Canteen", 100),
               ("Auditorium", 180)],
    "Admin": [("Canteen", 260), ("Auditorium", 120)],
    "Auditorium": [("Lab", 350), ("Hostel", 180), ("Admin", 120)]
}

h = {
    "Gate": 400, "Library": 330, "Canteen": 240,
    "Lab": 280, "Hostel": 160, "Admin": 110,
    "Auditorium": 0
}

def greedy(start, goal):
    current = start
    visited = {start}
    path = [start]
    distance = 0

    while current != goal:
        choices = [
            (h[n], n, cost)
            for n, cost in graph[current]
            if n not in visited
        ]

        if not choices:
            return None, None

        _, nxt, cost = min(choices)
        distance += cost
        current = nxt
        visited.add(current)
        path.append(current)

    return path, distance

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g != best[node]:
            continue

        for nxt, cost in graph[node]:
            new_g = g + cost

            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(
                    queue,
                    (new_g + h[nxt], new_g, nxt, path + [nxt])
                )

    return None, None

print("Greedy:", greedy("Gate", "Auditorium"))
print("A*:", astar("Gate", "Auditorium"))
