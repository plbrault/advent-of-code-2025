def parse_file(filename):
    return [
        [
            (int(value) if value.isnumeric() else value)
            for value in line.replace('\n', '').split(' ') if value != ''
        ]
        for line in open(filename, 'r').readlines()
    ]

def solve_worksheet(worksheet):
    for col_id in range(len(worksheet[0])):
        operation = worksheet[len(worksheet) - 1][col_id]
        print(operation)

data = parse_file('input.txt')
solve_worksheet(data)
#print(parse_file('input.txt'))
