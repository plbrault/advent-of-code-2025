junction_boxes = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

print(junction_boxes)
