def parse_file(filename):
    file_lines = open(filename).readlines()
    machines = []
    for line in file_lines:
        light_diagram = [character == '#'
            for character in line[:line.index(']')].replace('[','').replace(']','')]
        buttons = [
            eval(button) for button
                in line[line.index(']') + 1 : line.index('{') - 1].split(' ') if button != ''
        ]
        machines.append((light_diagram, buttons))
    return machines

print(parse_file('input.txt'))
