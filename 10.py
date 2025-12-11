def parse_file(filename):
    file_lines = open(filename).readlines()
    machines = []
    for line in file_lines:
        light_diagram = [character == '#'
            for character in line[1:line.index(']')]]
        buttons = [
            eval(button) for button
                in line[line.index(']') + 1 : line.index('{') - 1]
                    .replace('(','[').replace(')',']').split(' ') if button != ''
        ]
        joltages = [
            int(value)
            for value in line[line.index('{') + 1 : line.index('}')].split(',')
        ]
        machines.append((light_diagram, buttons, joltages))
    return machines

machines = parse_file('input.txt')

def start_machine(machine):
    diagram, buttons, joltages = machine

    min_num_presses_lights = float('inf')
    min_num_presses_joltages = float('inf')
    for i in range(2 ** len(buttons)):
        button_states = [bool(int(bit)) for bit in bin(i)[2:].zfill(len(buttons))]
        pressed_buttons = [button for button_id, button
            in enumerate(buttons) if button_states[button_id]]

        light_states = [False for _ in range(len(diagram))]
        for pressed_button in pressed_buttons:
            for light in list(pressed_button):
                light_states[light] = not light_states[light]

        if light_states == diagram:
            min_num_presses_lights = min(min_num_presses_lights,
                len([state for state in button_states if state is True]))

    return min_num_presses_lights, min_num_presses_joltages

results = [start_machine(machine) for machine in machines]
print('Result (part 1):', sum([result[0] for result in results]))
print('Result (part 2):', sum([result[1] for result in results]))
