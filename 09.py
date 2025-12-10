tiles = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        width = abs(tile2[0] - tile1[0]) + 1
        height = abs(tile2[1] - tile1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)

x_values_per_y = {}
y_values_per_x = {}

for tile in tiles:
    if tile[0] not in y_values_per_x:
        y_values_per_x[tile[0]] = []
    if tile[1] not in x_values_per_y:
        x_values_per_y[tile[1]] = []
    x_values_per_y[tile[1]].append(tile[0])
    y_values_per_x[tile[0]].append(tile[1])

for x in y_values_per_x:
    y_values_per_x[x] = sorted(y_values_per_x[x])
for y in x_values_per_y:
    x_values_per_y[y] = sorted(x_values_per_y[y])

largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        x1, y1 = tile1
        x2, y2 = tile2

        tile1_2 = (x1, y2)
        tile2_1 = (x2, y1)

        if (
            (tile1_2[0] < x_values_per_y[tile1_2[1]][0]
                or tile1_2[0] > x_values_per_y[tile1_2[1]][-1])
            and
            (tile1_2[1] < y_values_per_x[tile1_2[0]][0]
                or tile1_2[1] > y_values_per_x[tile1_2[0]][-1])
        ):
            continue
        if (
            (tile2_1[0] < x_values_per_y[tile2_1[1]][0]
                or tile2_1[0] > x_values_per_y[tile2_1[1]][-1])
            and
            (tile2_1[1] < y_values_per_x[tile2_1[0]][0]
                or tile2_1[1] > y_values_per_x[tile2_1[0]][-1])
        ):
            continue

        #print(tile1, tile2)

        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 2):', largest_area)
