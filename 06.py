from functools import reduce
from math import log10

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

    data = parse_file(input_filename)
    print('Result (part 1):', solve_worksheet(data))

def solve_part2(input_filename):
    def get_column_lengths(filename):
        matrix = [
            [
                (int(value) if value.isnumeric() else value)
                for value in line.replace('\n', '').split(' ') if value != ''
            ]
            for line in open(filename, 'r').readlines()
        ]
        return [
            max(
                int(log10(value)) + 1 for value in
                [matrix[row_id][col_id] for row_id in range(len(matrix) - 1)]
            )
                for col_id in range(len(matrix[0]))
        ]

    def read_columns(filename, column_lengths):
        matrix = [
            [
                (int(value) if value.isnumeric() else value)
                for value in list(line.replace('\n', ''))
            ]
            for line in open(filename, 'r').readlines()
        ]
        columns = {}
        for row in matrix[:-1]:
            col_id = 0
            local_id = 0
            for value in row:
                if local_id == column_lengths[col_id]:
                    col_id += 1
                    local_id = 0
                    continue
                print(value, column_lengths[col_id], col_id, local_id)
                local_id += 1

    read_columns(input_filename, get_column_lengths(input_filename))

solve_part1('input.txt')
solve_part2('input.txt')
