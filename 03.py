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

def find_first_battery(bank):
    return max(bank[:-1])

banks = parse_file('input.txt')

for bank in banks:
    print(find_first_battery(bank))
