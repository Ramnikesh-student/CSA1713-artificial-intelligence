
# Map Coloring using CSP, MRV and Forward Checking

colors = ['R', 'G', 'B']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW']
}

order = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
domains = {r: colors[:] for r in order}
assignment = {}

def solve():
    if len(assignment) == len(order):
        return True

    unassigned = [r for r in order if r not in assignment]

    # MRV, then degree heuristic, then given order
    region = min(
        unassigned,
        key=lambda r: (
            len(domains[r]),
            -sum(n in unassigned for n in neighbors[r]),
            order.index(r)
        )
    )

    for color in colors:
        if color not in domains[region]:
            continue

        assignment[region] = color
        saved = {r: domains[r][:] for r in unassigned}

        valid = True

        for n in neighbors[region]:
            if n not in assignment and color in domains[n]:
                domains[n].remove(color)

                if not domains[n]:
                    valid = False
                    break

        if valid and solve():
            return True

        del assignment[region]
        for r in saved:
            domains[r] = saved[r]

    return False

if solve():
    print("Final Coloring:")
    for r in order:
        print(r, ":", assignment[r])
else:
    print("No solution exists")
