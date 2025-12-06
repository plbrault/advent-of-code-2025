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


def count_fresh_ingredients(fresh_ranges, available_ids):
    return len({
        available_id for available_id in available_ids
            for fresh_range in fresh_ranges
                if fresh_range[0] <= available_id <= fresh_range[1]
    })

fresh_ranges, available_ids = parse_file('input.txt')

print('Result (part 1):', count_fresh_ingredients(fresh_ranges, available_ids))
