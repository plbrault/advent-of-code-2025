START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'
BEAM = '|'

def get_navigation_functions(matrix):
    def west(pos):
        row, col = pos
        return (row, col - 1) if col > 0 else None

    def south(pos):
        row, col = pos
        return (row + 1, col) if row < len(matrix) - 1 else None

    def east(pos):
        row, col = pos
        return (row, col + 1) if col < len(matrix[0]) - 1 else None

    return (west, south, east)

def get_start_pos(matrix):
    return (0, matrix[0].index(START))

def value(matrix, pos):
    if not pos:
        return None
    row, col = pos
    return matrix[row][col]

def update(matrix, pos, value):
    row, col = pos
    matrix[row][col] = value

def copy(matrix):
    return [row[:] for row in matrix]

def matrix_to_str(matrix):
    return '\n'.join([''.join(row) for row in matrix])

def print_matrix(matrix):
    print(matrix_to_str(matrix))

def solve_part1(matrix):
    start_pos = get_start_pos(matrix)
    west, south, east = get_navigation_functions(matrix)

    def move_beam(beam):
        if value(matrix, south(beam)) == EMPTY_SPACE:
            update(matrix, south(beam), BEAM)
            return move_beam(south(beam))
        elif value(matrix, south(beam)) == SPLITTER:
            return split(south(beam))
        return 0

    def split(splitter):
        new_beams = []
        if value(matrix, west(splitter)) == EMPTY_SPACE:
            update(matrix, west(splitter), BEAM)
            new_beams.append(west(splitter))
        if value(matrix, east(splitter)) == EMPTY_SPACE:
            update(matrix, east(splitter), BEAM)
            new_beams.append(east(splitter))
        splits = 0 if len(new_beams) == 0 else 1
        for beam in new_beams:
            splits += move_beam(beam)
        return splits

    print('Result (part 1):', move_beam(start_pos))

def solve_part2(matrix):
    start_pos = get_start_pos(matrix)
    west, south, east = get_navigation_functions(matrix)

    def move_beam(beam):
        if value(matrix, south(beam)) == EMPTY_SPACE:
            return move_beam(south(beam))
        elif value(matrix, south(beam)) == SPLITTER:
            return split(south(beam))
        elif south(beam) is None:
            return 1
        return 0

    def split(splitter):
        timelines = 0
        if value(matrix, west(splitter)) == EMPTY_SPACE:
            timelines += move_beam(west(splitter))
        if value(matrix, east(splitter)) == EMPTY_SPACE:
            timelines += move_beam(east(splitter))
        return timelines

    print('Result (part 2):', move_beam(start_pos))

matrix_1 = [list(line.replace('\n','')) for line in open('input.txt').readlines()]
matrix_2 = copy(matrix_1)
solve_part1(matrix_1)
solve_part2(matrix_2)
