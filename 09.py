coords = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

largest_area = 0
for coord1 in coords:
    for coord2 in coords:
        width = abs(coord2[0] - coord1[0]) + 1
        height = abs(coord2[1] - coord1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)
