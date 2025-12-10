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
        tile1_x, tile1_y = tile1
        tile2_x, tile2_y = tile2

        if (
            ((x_values[0] == tile1_x or x_values[-1] == tile1_x)
                and (y_values[0] == tile2_y or y_values[-1] == tile2_y))
            or
            ((x_values[0]) == tile2_x or x_values[-1] == tile2_x)
                and (y_values[0] == tile1_y or y_values[-1] == tile1_y)
        ):
            continue

        width = abs(tile2_x - tile1_x) + 1
        height = abs(tile2_y - tile1_y) + 1
        print(tile1, tile2, width, height, width * height)
        largest_area = max(largest_area, width * height)

print('Result (part 2):', largest_area)
