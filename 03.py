def parse_file(filename):
    banks = []
    with open(filename, 'r') as file:
        for row in file:
            bank = []
            for value in row:
                if value.isdigit():
                    bank.append(int(value))
            banks.append(bank)
    return banks

banks = parse_file('input.txt')

def solve_part1():
    joltage = 0
    for bank in banks:
        first_battery = max(bank[:-1])
        first_battery_id = bank.index(first_battery)
        second_battery = max(bank[(first_battery_id + 1):])
        joltage += first_battery * 10 + second_battery
    print('Result (part 1):', joltage)

def solve_part2():
    #for bank in banks:
    pass


solve_part1()
solve_part2()
