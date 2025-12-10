tiles = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        width = abs(tile2[0] - tile1[0]) + 1
        height = abs(tile2[1] - tile1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)

tiles_per_y = {}
tiles_per_x = {}

for tile in tiles:
    if tile[1] not in tiles_per_y:
        tiles_per_y[tile[1]] = []
    if tile[0] not in tiles_per_x:
        tiles_per_x[tile[0]] = []
    tiles_per_y[tile[1]].append(tile)
    tiles_per_x[tile[0]].append(tile)

for x in tiles_per_x:
    tiles_per_x[x] = sorted(tiles_per_x[x], key=lambda tile: tile[1])
for y in tiles_per_y:
    tiles_per_y[y] = sorted(tiles_per_y[y], key=lambda tile: tile[0])

x_values = sorted(list(tiles_per_x.keys()))
y_values = sorted(list(tiles_per_y.keys()))

largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        x1, y1 = tile1
        x2, y2 = tile2

        tile1_2 = (x1, y2)
        tile2_1 = (x2, y1)

        if (
            (tile1_2[0] < x_values[0] or tile1_2[0] > x_values[-1])
            and
            (tile1_2[1] < y_values[0] or tile1_2[0] > x_values[-1])
        ):
            continue
        if (
            (tile2_1[0] < x_values[0] or tile2_1[0] > x_values[-1])
            and
            (tile2_1[1] < y_values[0] or tile2_1[0] > x_values[-1])
        ):
            continue

        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        if width * height == 50:
            print(tile1, tile2, tile1_2, tile2_1, 
            x_values[-1])
        largest_area = max(largest_area, width * height)

print('Result (part 2):', largest_area)
