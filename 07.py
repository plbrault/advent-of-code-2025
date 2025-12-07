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

def print_matrix():
    print('\n'.join([''.join(row) for row in matrix]))

def solve_part1():
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

    print('Result (part 1):', move_beam())

solve_part1()
