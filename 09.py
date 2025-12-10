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

rows = sorted(list(tiles_per_y.keys()))
cols = sorted(list(tiles_per_x.keys()))

for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        tile1_x, tile1_y = tile1
        tile2_x, tile2_y = tile2
        #print(tile1_x, tile1_y, tile2_x, tile2_y)
