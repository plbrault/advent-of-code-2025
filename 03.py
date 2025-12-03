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

print(banks)
