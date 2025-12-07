matrix = [list(line.replace('\n','')) for line in open('input.txt').readlines()]

START = 'S'
EMPTY_SPACE = '.'
SPLITTER = '^'

start_pos = (0, matrix[0].index(START))

print(start_pos)
