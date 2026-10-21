
# Greedy Best-First Search

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

open_list = [('S', ['S'], 0)]
visited = set()

while open_list:
    open_list.sort(key=lambda x: h[x[0]])
    node, path, cost = open_list.pop(0)

    if node in visited:
        continue

    visited.add(node)

    if node == 'G':
        print("Path:", path)
        print("Total cost:", cost)
        break

    for neighbor, edge_cost in graph[node]:
        if neighbor not in visited:
            open_list.append(
                (neighbor, path + [neighbor], cost + edge_cost)
            )

    print("Expanded:", node,
          "OPEN:", [(n, h[n]) for n, _, _ in
                    sorted(open_list, key=lambda x: h[x[0]])])
