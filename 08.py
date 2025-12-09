import numpy as np

junction_boxes = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

distances = {}
for i, junction_box in enumerate(junction_boxes):
    for _, other_junction_box in enumerate(junction_boxes[i + 1:]):
        distances[(junction_box, other_junction_box)] = np.linalg.norm(
            np.array(junction_box) - np.array(other_junction_box))

sorted_distances = {key: value for key, value in sorted(distances.items(), key=lambda item: item[1])}
