
# A* Search Algorithm

import heapq

graph = {
    'S': [('A', 2), ('B', 3)],
    'A': [('S', 2), ('C', 4), ('D', 7)],
    'B': [('S', 3), ('D', 2), ('E', 6)],
    'C': [('A', 4), ('G', 6)],
    'D': [('A', 7), ('B', 2), ('G', 3)],
    'E': [('B', 6), ('G', 2)],
    'G': [('C', 6), ('D', 3), ('E', 2)]
}

h = {'S': 7, 'A': 8, 'B': 4, 'C': 5,
     'D': 3, 'E': 2, 'G': 0}

pq = [(h['S'], 0, 'S', ['S'])]
best_cost = {'S': 0}

while pq:
    f, g, node, path = heapq.heappop(pq)

    if g != best_cost[node]:
        continue

    print("Expanded:", node)

    if node == 'G':
        print("Path:", path)
        print("Total cost:", g)
        break

    for neighbor, cost in graph[node]:
        new_g = g + cost

        if new_g < best_cost.get(neighbor, float('inf')):
            best_cost[neighbor] = new_g
            new_f = new_g + h[neighbor]

            heapq.heappush(
                pq, (new_f, new_g, neighbor,
                     path + [neighbor])
            )
