import textwrap

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

def is_invalid(id, max_repeats=float('inf')):
    num_digits = len(id)
    for divisor in range(2, num_digits + 1):
        quotient = num_digits / divisor
        if quotient.is_integer():
            parts = textwrap.wrap(id, int(num_digits / divisor))
            return (len(set(parts)) == 1 and len(parts) <= max_repeats)
    return False

ranges = parse_file('input.txt')
ids = get_individual_ids(ranges)

part1_result = sum([int(id) for id in ids if is_invalid(id, 2)])
print('Result for part 1:', part1_result)

part2_result = sum([int(id) for id in ids if is_invalid(id)])
print('Result for part 2:', part2_result)
