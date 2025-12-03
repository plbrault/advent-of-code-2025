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

def is_invalid(id):
    num_digits = len(id)
    for divisor in range(2, num_digits + 1):
        quotient = num_digits / divisor
        if (num_digits / divisor).is_integer():
            parts = textwrap.wrap(id, int(num_digits / divisor))
            if (len(set(parts)) == 1):
                print(parts)

ranges = parse_file('input.txt')
ids = get_individual_ids(ranges)

for id in ids:
    is_invalid(id)
