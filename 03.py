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
    NUM_BATTERIES = 12
    total_joltage = 0
    for bank in banks:
        next_id = 0
        joltage = 0
        for num_after in range(NUM_BATTERIES - 1, -1, -1):
            sub_bank = bank[next_id:(-num_after if num_after > 0 else None)]
            if len(sub_bank) == 0:
                break
            battery = max(sub_bank)
            next_id += sub_bank.index(battery) + 1
            joltage += battery * 10 ** num_after
        total_joltage += joltage
    print('Result (part 2):', total_joltage)

solve_part1()
solve_part2()
