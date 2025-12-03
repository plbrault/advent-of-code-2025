def parse_file(filename):
    with open(filename, 'r') as input_file:
        ranges = [r.replace('\n','').split('-') for r in input_file.readline().split(',')]
        return ranges

def get_individual_ids(ranges):
    ids = []
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            ids.append(str(i))
    return ids

ranges = parse_file('input.txt')
ids = get_individual_ids(ranges)

print(ids)
