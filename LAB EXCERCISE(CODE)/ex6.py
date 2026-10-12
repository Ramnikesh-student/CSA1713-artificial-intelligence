
# Vacuum Cleaner Problem

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while True:
    print("Current Room:", location)
    print("Room Status:", rooms[location])

    if rooms[location] == 'Dirty':
        rooms[location] = 'Clean'
        print("Cleaning Room", location)

    if location == 'A':
        location = 'B'
    else:
        break

print("\nFinal Room Status:", rooms)
