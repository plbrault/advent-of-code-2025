def parse_file(filename):
    fresh_ranges = []
    available_ids = []
    with open(filename, 'r') as file:
        line = file.readline().replace('\n', '')
        while line != '':
            start, end = [int(value) for value in line.split('-')]
            fresh_ranges.append((start, end))
            line = file.readline().replace('\n', '')
        for line in file:
            available_ids.append(int(line))
    return fresh_ranges, available_ids

print(parse_file('input.txt'))
