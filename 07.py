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

def value(pos):
    row, col = pos
    return matrix[row][col]

def update(pos, value):
    row, col = pos
    matrix[row][col] = value

def move_beam(beam=start_pos):
    if value(south(beam)) == EMPTY_SPACE:
        update(south(beam), BEAM)
        move_beam(south(beam))
    elif value(south(beam)) == SPLITTER:
        if southwest(beam) and value(southwest(beam)) != BEAM:
            if value(southwest(beam)) == EMPTY_SPACE:
                update(south(beam), BEAM)
                move_beam(south(beam))
                return 0
            elif value(southwest(beam)) == SPLITTER:
                return split(southwest(beam))
    return 0

def split(splitter):
    pass
