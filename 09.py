tiles = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]


rectangles = []
largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        rectangles.append([tile1, tile2])
        width = abs(tile2[0] - tile1[0]) + 1
        height = abs(tile2[1] - tile1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)
