def parse_file(filename):
    return [
        [
            (int(value) if value.isnumeric() else value)
            for value in line.replace('\n', '').split(' ') if value != ''
        ]
        for line in open(filename, 'r').readlines()
    ]

print(parse_file('input.txt'))
