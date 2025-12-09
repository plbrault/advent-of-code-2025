PART1_NUM_CONNECTIONS_TO_USE = 1000
PART1_NUM_CIRCUITS_TO_KEEP = 3

from datetime import datetime
import numpy as np
from functools import reduce

def create_connection_graph(connections):
    graph = {}
    for junction_box_1, junction_box_2 in connections:
        if junction_box_1 not in graph:
            graph[junction_box_1] = []
        if junction_box_2 not in graph:
            graph[junction_box_2] = []
        graph[junction_box_1].append(junction_box_2)
        graph[junction_box_2].append(junction_box_1)
    return graph

def compute_circuits(connection_graph):
    circuits = []
    processed_boxes = set()

    def build_circuit(junction_box, circuit):
        processed_boxes.add(junction_box)
        circuit.add(junction_box)

        for other_junction_box in connection_graph[junction_box]:
            if other_junction_box not in processed_boxes:
                build_circuit(other_junction_box, circuit)

    for junction_box in connection_graph:
        if junction_box not in processed_boxes:
            circuit = set()
            build_circuit(junction_box, circuit)
            circuits.append(circuit)

    return circuits

junction_boxes = [tuple([int(value) for value in line.split(',')]) for line in open('input.txt').readlines()]

print('Calculating distances...')
distances = {}
for i, junction_box in enumerate(junction_boxes):
    for _, other_junction_box in enumerate(junction_boxes[i + 1:]):
        distances[(junction_box, other_junction_box)] = np.linalg.norm(
            np.array(junction_box) - np.array(other_junction_box))

print('Sorting distances...')
sorted_distances = {key: value for key, value in sorted(distances.items(), key=lambda item: item[1])}

def solve_part1():
    print('=== PART 1 ===')

    print('Creating connection graph...')
    connections_to_use = list(sorted_distances.keys())[:PART1_NUM_CONNECTIONS_TO_USE]
    connection_graph = create_connection_graph(connections_to_use)

    print('Computing circuits...')
    circuits = compute_circuits(connection_graph)
    sorted_circuit_sizes = sorted([len(circuit) for circuit in circuits], reverse=True)

    print('Result (part 1):', reduce(
        lambda acc, circuit_size : acc * circuit_size,
        sorted_circuit_sizes[:PART1_NUM_CIRCUITS_TO_KEEP])
    )

def solve_part2():
    print('=== PART 2 ===')

    for num_connections_to_use in range(PART1_NUM_CONNECTIONS_TO_USE + 1, len(distances)):
        connections_to_use = list(sorted_distances.keys())[:num_connections_to_use]
        print('Adding connection:', connections_to_use[-1])

        print(f'Creating connection graph with {num_connections_to_use} connections...')
        connection_graph = create_connection_graph(connections_to_use)

        print(f'Computing circuits with {num_connections_to_use} connections...')
        circuits = compute_circuits(connection_graph)

        print('Number of circuits:', len(circuits))

        if len(circuits) == 1:
            circuit_size = len(circuits[0])
            print('Circuit size:', circuit_size)
            if circuit_size == len(junction_boxes):
                print('Found solution')
                print('Result (part 2):',
                    connections_to_use[-1][0][0] * connections_to_use[-1][1][0])
                break

start_time = datetime.now()
solve_part1()
solve_part2()
end_time = datetime.now()
print('Completed in', (end_time - start_time).total_seconds(), 'seconds.')
