# Exam Scheduling using Plain Backtracking

courses = ["A", "B", "C", "D", "E"]

slots = ["Slot1", "Slot2", "Slot3"]

# Conflicting course pairs
conflicts = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E")
]


# Check whether assigning a slot is valid
def is_valid(course, slot, assignment):

    for course1, course2 in conflicts:

        if course == course1:
            other = course2

        elif course == course2:
            other = course1

        else:
            continue

        if other in assignment:
            if assignment[other] == slot:
                return False

    return True


# Plain Backtracking
def backtracking(assignment):

    # All courses assigned
    if len(assignment) == len(courses):
        return assignment

    # Static variable order
    course = courses[len(assignment)]

    # Slot order: Slot1, Slot2, Slot3
    for slot in slots:

        print("Trying:", course, "=", slot)

        if is_valid(course, slot, assignment):

            assignment[course] = slot

            result = backtracking(assignment)

            if result is not None:
                return result

            # Backtrack
            print("Backtracking from:", course, "=", slot)
            del assignment[course]

        else:
            print("Conflict found")

    return None


solution = backtracking({})

print("\nFinal Timetable:")

for course in courses:
    print(course, "=", solution[course])
