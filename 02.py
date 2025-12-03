def parse_file(filename):
    with open(filename, 'r') as input_file:
        ranges = [range.replace('\n','').split('-') for range in input_file.readline().split(',')]
        return ranges

print(parse_file('input.txt'))
