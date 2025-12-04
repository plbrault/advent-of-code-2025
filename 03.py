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

def solve(num_batteries):
    total_joltage = 0
    for bank in banks:
        next_id = 0
        joltage = 0
        for num_after in range(num_batteries - 1, -1, -1):
            sub_bank = bank[next_id:(-num_after if num_after > 0 else None)]
            if len(sub_bank) == 0:
                break
            battery = max(sub_bank)
            next_id += sub_bank.index(battery) + 1
            joltage += battery * 10 ** num_after
        total_joltage += joltage
    return total_joltage

print('Result (part 1):', solve(2))
print('Result (part 2):', solve(12))
