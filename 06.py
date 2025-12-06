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
    def get_column_count_per_problem(filename):
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

    def parse_numbers(filename):
        matrix = [
            [
                value
                for value in list(line.replace('\n', ''))
            ]
            for line in open(filename, 'r').readlines()
        ]
        numbers = []
        for matrix_col_id in range(len(matrix[0])):
            number_str = ''.join([
                matrix[matrix_row_id][matrix_col_id] for matrix_row_id in range(len(matrix) - 1)
            ]).strip()
            if number_str:
                numbers.append(int(number_str))
        return numbers

    def parse_operators(filename):
        return [
            [value for value in line.replace('\n', '').split(' ') if value != '']
            for line in open(filename, 'r').readlines()
        ][-1]

    def solve_problems(column_count_per_problem, numbers, operators):
        number_iterator = iter(numbers)
        for column_count in column_count_per_problem:
            print([next(number_iterator) for i in range(column_count)])

    column_count_per_problem = get_column_count_per_problem(input_filename)
    numbers = parse_numbers(input_filename)
    operators = parse_operators(input_filename)

    print('Result (part 2)', solve_problems(column_count_per_problem, numbers, operators))



solve_part1('input.txt')
solve_part2('input.txt')
