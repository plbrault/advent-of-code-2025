def parse_file(filename):
    fresh_ranges = []
    available_ids = []
    with open(filename, 'r') as file:
        line = file.readline().replace('\n', '')
        while line != '':
            id_range = [int(value) for value in line.split('-')]
            fresh_ranges.append(id_range)
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

def merge_intersecting_ranges(id_ranges):
    id_ranges.sort(key=lambda id_range: id_range[0])
    merged_ranges = []
    current_merge = id_ranges[0]
    for id_range in id_ranges[1:]:
        print(current_merge, id_range)
        if current_merge[0] <= id_range[0] and current_merge[1] >= id_range[0]:
            current_merge[1] = max(current_merge[1], id_range[1])
        else:
            merged_ranges.append(current_merge)
            current_merge = id_range
    merged_ranges.append(current_merge)
    return merged_ranges

fresh_ranges, available_ids = parse_file('input.txt')

print('Result (part 1):', count_fresh_ingredients(fresh_ranges, available_ids))

fresh_ranges = merge_intersecting_ranges(fresh_ranges)
print(fresh_ranges)
