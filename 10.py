def parse_file(filename):
    file_lines = open(filename).readlines()
    machines = []
    for line in file_lines:
        light_diagram = [character == '#'
            for character in line[:line.index(']')].replace('[','').replace(']','')]
        buttons = [
            eval(button) for button
                in line[line.index(']') + 1 : line.index('{') - 1]
                    .replace('(','[').replace(')',']').split(' ') if button != ''
        ]
        machines.append((light_diagram, buttons))
    return machines

machines = parse_file('input.txt')

def start_machine(machine):
    diagram, buttons = machine
    
    min_num_presses = float('inf')
    for i in range(len(buttons) ** 2):
        button_states = [bool(int(bit)) for bit in bin(i)[2:].zfill(len(buttons))]
        pressed_buttons = [button for button_id, button
            in enumerate(buttons) if button_states[button_id]]

        light_states = [False for _ in range(len(diagram))]
        for pressed_button in pressed_buttons:
            for light in list(pressed_button):
                light_states[light] = not light_states[light]

        if light_states == diagram:
            min_num_presses = min(min_num_presses,
                len([state for state in light_states if state is True]))

    return min_num_presses

print(start_machine(machines[0]))
