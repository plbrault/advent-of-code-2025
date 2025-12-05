def parse_file(filename):
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            arr.append([character for character in line if character != '\n'])
    return arr

arr = parse_file('input.txt')

def count_accessible_rolls():
    ROLL = '@'

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

    accessible_rolls = 0

    for y, row in enumerate(arr):
        for x, value in enumerate(row):
            if value == ROLL:
                num_adjacent_rolls = 0
                for (dy, dx) in deltas:
                    if (
                        y + dy >= 0
                        and y + dy < len(arr)
                        and x + dx >= 0
                        and x + dx < len(row)
                        and arr[y + dy][x + dx] == ROLL
                    ):
                        num_adjacent_rolls += 1
                        if num_adjacent_rolls == 4:
                            break
                if num_adjacent_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls

print('Result (part 1):', count_accessible_rolls())
