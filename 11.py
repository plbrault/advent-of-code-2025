graph = {}
for line in open('input.txt').readlines():
    node, neighbours_str = line.replace('\n','').split(': ')
    neighbours = neighbours_str.split(' ')
    graph[node] = neighbours

memo = {}

def find_paths(start, end, visited_nodes=None):
    if (start, end) in memo:
        return memo[(start, end)]

    if not visited_nodes:
        visited_nodes = {start}
    num_paths = 0
    if start not in graph:
        return num_paths
    for neighbour in graph[start]:
        if neighbour in visited_nodes:
            continue
        if neighbour == end:
            num_paths += 1
        else:
            num_paths += find_paths(neighbour, end, visited_nodes)

    memo[(start, end)] = num_paths
    return num_paths

print('Result (part 1):', find_paths('you', 'out'))
