import numpy as np

NUM_CIRCUITS = 10

junction_boxes = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

print('Calculating distances...')

distances = {}
for i, junction_box in enumerate(junction_boxes):
    for _, other_junction_box in enumerate(junction_boxes[i + 1:]):
        distances[(junction_box, other_junction_box)] = np.linalg.norm(
            np.array(junction_box) - np.array(other_junction_box))

print('Sorting distances...')
sorted_distances = {key: value for key, value in sorted(distances.items(), key=lambda item: item[1])}

print('Creating graph of junction boxes...')
graph = {}
for junction_box_1, junction_box_2 in list(distances.keys())[:NUM_CIRCUITS]:
    if junction_box_1 not in graph:
        graph[junction_box_1] = []
    if junction_box_2 not in graph:
        graph[junction_box_2] = []
    graph[junction_box_1].append(junction_box_2)
    graph[junction_box_2].append(junction_box_1)
