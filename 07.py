def parse_input(filename):
    return [list(line.replace('\n','')) for line in open(filename).readlines()]

print(parse_input('input.txt'))
