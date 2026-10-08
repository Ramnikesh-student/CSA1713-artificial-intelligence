# Exam Scheduling using Forward Checking

courses = ["A", "B", "C", "D", "E"]

slots = ["Slot1", "Slot2", "Slot3"]

conflicts = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E")
]


# Check whether two courses conflict
def are_conflicting(course1, course2):

    return ((course1, course2) in conflicts or
            (course2, course1) in conflicts)


# Forward Checking
def forward_check(assignment, domains):

    # All courses assigned
    if len(assignment) == len(courses):
        return assignment

    # Static variable order
    course = courses[len(assignment)]

    # Try Slot1, Slot2, Slot3
    for slot in domains[course]:

        print("Trying:", course, "=", slot)

        # Check current assignment
        valid = True

        for assigned_course in assignment:

            if are_conflicting(course, assigned_course):

                if assignment[assigned_course] == slot:
                    valid = False
                    break

        if not valid:
            print("Conflict found")
            continue

        # Make a copy of domains
        new_domains = {}

        for c in domains:
            new_domains[c] = domains[c].copy()

        # Assign the course
        assignment[course] = slot

        # Remove the selected slot from neighbors
        failed = False

        for other in courses:

            if other == course:
                continue

            if are_conflicting(course, other):

                if slot in new_domains[other]:
                    new_domains[other].remove(slot)

                # Empty domain means failure
                if len(new_domains[other]) == 0:
                    failed = True
                    break

        if not failed:

            result = forward_check(
                assignment,
                new_domains
            )

            if result is not None:
                return result

        # Backtrack
        print("Backtracking from:", course, "=", slot)

        del assignment[course]

    return None


# Initial domains
domains = {}

for course in courses:
    domains[course] = slots.copy()


solution = forward_check({}, domains)

print("\nFinal Timetable:")

for course in courses:
    print(course, "=", solution[course])
