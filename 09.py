tiles = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

largest_area = 0
for tile1 in tiles:
    for tile2 in tiles:
        width = abs(tile2[0] - tile1[0]) + 1
        height = abs(tile2[1] - tile1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)

tiles_per_row = {}
tiles_per_col = {}

for tile in tiles:
    if tile[1] not in tiles_per_row:
        tiles_per_row[tile[1]] = []
    if tile[0] not in tiles_per_col:
        tiles_per_col[tile[0]] = []
    tiles_per_row[tile[1]].append(tile)
    tiles_per_col[tile[0]].append(tile)

for row in tiles_per_row:
    tiles_per_row[row] = sorted(tiles_per_row[row], key=lambda tile: tile[0])
for col in tiles_per_col:
    tiles_per_col[col] = sorted(tiles_per_col[col], key=lambda tile: tile[1])
