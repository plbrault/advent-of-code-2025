def parse_file(filename):
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            arr.append([character for character in line if character != '\n'])
    return arr

arr = parse_file('input.txt')

ROLL = '@'
NO_ROLL = '.'

deltas = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def in_bounds(y, x):
    return y >= 0 and y < len(arr) and x >= 0 and x < len(arr[0])

def can_access_roll(y, x):
    num_adjacent_rolls = 0
    for (dy, dx) in deltas:
        if in_bounds(y + dy, x + dx) and arr[y + dy][x + dx] == ROLL:
            num_adjacent_rolls += 1
            if num_adjacent_rolls == 4:
                break
    return num_adjacent_rolls < 4

def count_accessible_rolls():
    accessible_rolls = 0
    for y, row in enumerate(arr):
        for x, value in enumerate(row):
            if value == ROLL and can_access_roll(y, x):
                accessible_rolls += 1
    return accessible_rolls

def remove_rolls_from(y, x):
    arr[y][x] = NO_ROLL
    removed_rolls = 1
    for (dy, dx) in deltas:
        if (
            in_bounds(y + dy, x + dx)
            and arr[y + dy][x + dx] == ROLL
            and can_access_roll(y + dy, x + dx)
        ):
            removed_rolls += remove_rolls_from(y + dy, x + dx)
    return removed_rolls

def remove_rolls():
    for y, row in enumerate(arr):
        for x, value in enumerate(row):
            if value == ROLL and can_access_roll(y, x):
                remove_rolls_from(y, x)

print('Result (part 1):', count_accessible_rolls())

remove_rolls()
