
from itertools import permutations

# Cost matrix representing distances between cities
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
cities = list(range(n))

min_cost = float('inf')
best_path = []

# Fix city 0 as the starting city
for path in permutations(cities[1:]):
    route = (0,) + path + (0,)
    total_cost = 0

    for i in range(len(route) - 1):
        total_cost += cost[route[i]][route[i + 1]]

    if total_cost < min_cost:
        min_cost = total_cost
        best_path = route

print("Minimum cost:", min_cost)
print("Best route:", " -> ".join(str(city) for city in best_path))
