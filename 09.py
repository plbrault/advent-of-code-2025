from shapely.geometry import Polygon

tiles = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

rectangles = []
largest_area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        x1, y1 = tile1
        x2, y2 = tile2
        rectangles.append(Polygon([ (x1, y1), (x2, y1), (x2, y2), (x1, y2) ]))
        width = abs(tile2[0] - tile1[0]) + 1
        height = abs(tile2[1] - tile1[1]) + 1
        largest_area = max(largest_area, width * height)

print('Result (part 1):', largest_area)

polygon = Polygon(tiles)

candidate_rectangles = [rectangle for rectangle in rectangles if polygon.contains(rectangle)]
largest_rectangle = sorted(candidate_rectangles, key=lambda rectangle: rectangle.area, reverse=True)[0]
x1, y1, x2, y2 = largest_rectangle.bounds
width = x2 - x1 + 1
height = y2 - y1 + 1
largest_area = int(width * height)

print('Result (part 2):', largest_area)
