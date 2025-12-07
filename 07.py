matrix = [list(line.replace('\n','')) for line in open('input.txt').readlines()]

START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'
BEAM = '|'

start_pos = (0, matrix[0].index(START))

def south(pos):
    row, col = pos
    return (row + 1, col) if row < len(matrix) - 1 else None

def southwest(pos):
    row, col = pos
    return (row + 1, col - 1) if (row < len(matrix) - 1 and col > 0) else None

def southeast(pos):
    row, col = pos
    return (row + 1, col + 1) if (row < len(matrix) - 1 and col < len(matrix[0]) - 1) else None

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

def move_beam(beam=start_pos):
    if value(south(beam)) == EMPTY_SPACE:
        update(south(beam), BEAM)
        return move_beam(south(beam))
    elif value(south(beam)) == SPLITTER:
        return split(south(beam))
    return 0

def split(splitter):
    splits = 0
    if value(west(splitter)) == EMPTY_SPACE:
        update(west(splitter), BEAM)
        splits += 1 + move_beam(west(splitter))
    elif value(west(splitter)) == SPLITTER:
        splits += split(west(splitter))
    if value(east(splitter)) == EMPTY_SPACE:
        update(east(splitter), BEAM)
        splits += 1 + move_beam(east(splitter))
    elif value(east(splitter)) == SPLITTER:
        splits += split(east(splitter))
    return splits

print('Result (part 1):', move_beam())
