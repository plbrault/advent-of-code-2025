import numpy as np
from functools import reduce

NUM_BOXES_TO_USE = 10
NUM_CIRCUITS_TO_KEEP = 3

junction_boxes = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

print('Calculating distances...')

distances = {}
for i, junction_box in enumerate(junction_boxes):
    for _, other_junction_box in enumerate(junction_boxes[i + 1:]):
        distances[(junction_box, other_junction_box)] = np.linalg.norm(
            np.array(junction_box) - np.array(other_junction_box))

print('Sorting distances...')
sorted_distances = {key: value for key, value in sorted(distances.items(), key=lambda item: item[1])}

boxes_to_use = list(sorted_distances.keys())[:NUM_BOXES_TO_USE]

print('Creating graph of junction boxes...')
graph = {}
for junction_box_1, junction_box_2 in boxes_to_use:
    if junction_box_1 not in graph:
        graph[junction_box_1] = []
    if junction_box_2 not in graph:
        graph[junction_box_2] = []
    graph[junction_box_1].append(junction_box_2)
    graph[junction_box_2].append(junction_box_1)


print('Computing circuits...')

circuits = []
processed_boxes = set()

def build_circuit(junction_box, circuit):
    processed_boxes.add(junction_box)
    circuit.add(junction_box)

    for other_junction_box in graph[junction_box]:
        if other_junction_box not in processed_boxes:
            build_circuit(other_junction_box, circuit)

for junction_box in graph:
    if junction_box not in processed_boxes:
        circuit = set()
        build_circuit(junction_box, circuit)
        circuits.append(circuit)

sorted_circuit_lengths = sorted([len(circuit) for circuit in circuits], reverse=True)

print('Result (part 1):', reduce(lambda acc, circuit_length : acc * circuit_length, sorted_circuit_lengths[:NUM_CIRCUITS_TO_KEEP]))
