graph = {}
for line in open('input.txt').readlines():
    node, neighbours_str = line.replace('\n','').split(': ')
    neighbours = neighbours_str.split(' ')
    graph[node] = neighbours

def find_paths(start, end, visited_nodes=set()):
    if not visited_nodes:
        visited_nodes = {start}
    num_paths = 0
    for neighbour in graph[start]:
        if neighbour in visited_nodes:
            continue
        if neighbour == end:
            num_paths += 1
        else:
            num_paths += find_paths(neighbour, end, visited_nodes)
    return num_paths

print('Result (part 1):', find_paths('you', 'out'))
