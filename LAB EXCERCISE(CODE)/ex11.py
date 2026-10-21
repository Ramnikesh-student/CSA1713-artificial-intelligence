
# Map Coloring using CSP

colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color_map = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            color_map[region] = color

            if solve(regions[1:]):
                return True

            del color_map[region]

    return False

if solve(list(graph.keys())):
    print("Map Coloring Solution:")
    for region, color in color_map.items():
        print(region, ":", color)
else:
    print("No solution exists")
