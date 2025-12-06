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

def generate_ids(id_ranges):
    return {
        id for id_range in id_ranges
            for id in range(id_range[0], id_range[1] + 1)
    }

def count_fresh_ingredients(fresh_ids, available_ids):
    return len([
        id for id in available_ids if id in fresh_ids
    ])

fresh_ranges, available_ids = parse_file('input.txt')
fresh_ids = generate_ids(fresh_ranges)

print('Result (part 1):', count_fresh_ingredients(fresh_ids, available_ids))
