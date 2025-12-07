matrix = [list(line.replace('\n','')) for line in open('input.txt').readlines()]

START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'
BEAM = '|'

start_pos = (0, matrix[0].index(START))

def north(pos):
    row, col = pos
    return (row - 1, col) if row > 0 else None

def northwest(pos):
    row, col = pos
    return (row - 1, col - 1) if (row > 0 and col > 0) else None

def northeast(pos):
    row, col = pos
    return (row - 1, col + 1) if (row > 0 and col < len(matrix[0]) - 1) else None

def south(pos):
    row, col = pos
    return (row + 1, col) if row < len(matrix) - 1 else None

def west(pos):
    row, col = pos
    return (row, col - 1) if col > 0 else None

def east(pos):
    row, col = pos
    return (row, col + 1) if col < len(matrix[0]) - 1 else None

def value(pos):
    if not pos:
        return None
    row, col = pos
    return matrix[row][col]

def update(pos, value):
    row, col = pos
    matrix[row][col] = value

def print_matrix():
    print('\n'.join([''.join(row) for row in matrix]))

def move_beam(beam=start_pos):
    if value(south(beam)) == EMPTY_SPACE:
        update(south(beam), BEAM)
        return move_beam(south(beam))
    elif value(south(beam)) == SPLITTER:
        return split(south(beam))
    return 0

def split(splitter):
    new_beams = []
    if value(west(splitter)) == EMPTY_SPACE:
        update(west(splitter), BEAM)
        new_beams.append(west(splitter))
    if value(east(splitter)) == EMPTY_SPACE:
        update(east(splitter), BEAM)
        new_beams.append(east(splitter))
    
    splits = 0 if len(new_beams) == 0 else 1
    for beam in new_beams:
        splits += move_beam(beam)
    return splits

def count_timelines():
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            pos = (i, j)
            if value(pos) == START:
                update(pos, 1)
            elif value(pos) == BEAM:
                timelines = 0
                if value(west(pos)) == SPLITTER:
                    timelines += value(northwest(pos)) if isinstance(value(northwest(pos)), int) else 0
                if value(east(pos)) == SPLITTER:
                    timelines += value(northeast(pos)) if isinstance(value(northeast(pos)), int) else 0
                if isinstance(value(north(pos)), int):
                    timelines += value(north(pos))
                update(pos, timelines)
    return sum([value for value in matrix[-1] if isinstance(value, int)])

print('Result (part 1):', move_beam())
print('Result (part 2):', count_timelines())
