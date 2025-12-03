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
    def find_first_battery(bank):
        return max(bank[:-1])

    def find_second_battery(bank, first_battery_id):
        return max(bank[(first_battery_id + 1):])

    total_joltage = 0
    for bank in banks:
        first_battery = find_first_battery(bank)
        first_battery_id = bank.index(first_battery)
        second_battery = find_second_battery(bank, first_battery_id)
        joltage = first_battery * 10 + second_battery
        total_joltage += joltage

    print('Result (part 1):', total_joltage)

solve_part1()
