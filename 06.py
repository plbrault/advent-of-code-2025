from functools import reduce

def solve_part1(input_filename):
    def parse_file(filename):
        return [
            [
                (int(value) if value.isnumeric() else value)
                for value in line.replace('\n', '').split(' ') if value != ''
            ]
            for line in open(filename, 'r').readlines()
        ]

    def solve_worksheet(worksheet):
        result = 0
        for col_id in range(len(worksheet[0])):
            operator = worksheet[len(worksheet) - 1][col_id]
            numbers = [row[col_id] for row in worksheet[:-1]]
            result += reduce(lambda acc, n : eval(f"{acc} {operator} {n}"), numbers)
        return result

    data = parse_file('input.txt')
    print('Result (part 1):', solve_worksheet(data))

solve_part1('input.txt')
