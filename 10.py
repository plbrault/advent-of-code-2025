from z3 import *

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

def solve_part_1():
    def start_machine(machine):
        diagram, buttons, _ = machine

        min_num_presses = float('inf')
        for i in range(2 ** len(buttons)):
            button_states = [bool(int(bit)) for bit in bin(i)[2:].zfill(len(buttons))]
            pressed_buttons = [button for button_id, button
                in enumerate(buttons) if button_states[button_id]]

            light_states = [False for _ in range(len(diagram))]
            for pressed_button in pressed_buttons:
                for light in list(pressed_button):
                    light_states[light] = not light_states[light]

            if light_states == diagram:
                min_num_presses = min(min_num_presses,
                    len([state for state in button_states if state is True]))

        return min_num_presses

    print('Result (part 1):', sum([start_machine(machine) for machine in machines]))

def solve_part_2():
    def start_machine(machine):
        _, buttons, joltages = machine

        # I want to solve A * x = b, where:
        #    - A is a matrix of button effects
        #        - Each row is a counter
        #        - Each column is a button
        #    - x is the vector of numbers of button presses
        #    - b is the vector of desired counter values (the `joltages` array)

        solver = Optimize()

        A = [[0 for _ in buttons] for _ in joltages]
        for button_id, button in enumerate(buttons):
            for counter in button:
                A[counter][button_id] = 1

        x = [Int(f'button_{i}') for i in range(len(buttons))]
        for button in x:
            solver.add(button >= 0)

        b = joltages

        for i in range(len(b)):
            solver.add(Sum(A[i][j] * x[j] for j in range(len(x))) == b[i])
        solver.minimize(Sum(x))

        if solver.check() == sat:
            model = solver.model()
            solution = [model.evaluate(button) for button in x]
            return sum([presses.as_long() for presses in solution])
        return float('inf')

    print('Result (part 2):', sum([start_machine(machine) for machine in machines]))

solve_part_1()
solve_part_2()
