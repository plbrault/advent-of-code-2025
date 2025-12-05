def parse_file(filename):
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            arr.append([character for character in line if character != '\n'])
    return arr

print(parse_file('input.txt'))
