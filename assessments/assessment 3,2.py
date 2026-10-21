
# Workshop Scheduling using CSP and Backtracking

slots = ["Morning", "Afternoon", "Evening"]

domains = {
    "W1": slots[:],
    "W2": slots[:],
    "W3": ["Afternoon", "Evening"],
    "W4": ["Morning", "Afternoon"],
    "W5": slots[:]
}

conflicts = {
    "W1": ["W2", "W3"],
    "W2": ["W1", "W3", "W4"],
    "W3": ["W1", "W2", "W5"],
    "W4": ["W2", "W5"],
    "W5": ["W3", "W4"]
}

assignment = {}

def valid(workshop, slot):
    for other in conflicts[workshop]:
        if assignment.get(other) == slot:
            return False
    return True

def solve():
    if len(assignment) == len(domains):
        return True

    unassigned = [w for w in domains if w not in assignment]

    # MRV, then highest number of unassigned conflicts,
    # then workshop number
    workshop = min(
        unassigned,
        key=lambda w: (
            sum(valid(w, s) for s in domains[w]),
            -sum(1 for n in conflicts[w] if n in unassigned),
            w
        )
    )

    for slot in slots:
        if slot in domains[workshop] and valid(workshop, slot):
            assignment[workshop] = slot

            if solve():
                return True

            del assignment[workshop]

    return False

if solve():
    print("Valid Timetable:")
    for w in sorted(assignment):
        print(w, ":", assignment[w])
else:
    print("No valid timetable exists")
