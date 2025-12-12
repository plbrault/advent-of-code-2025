graph = {}
for line in open('input.txt').readlines():
    node, neighbours_str = line.replace('\n','').split(': ')
    neighbours = neighbours_str.split(' ')
    graph[node] = neighbours

def find_paths(start, end):
    paths = []
    for neighbour in graph[start]:
        if neighbour == end:
            paths.append([start, end])
        else:
            paths += [([start] + path) for path in find_paths(neighbour, end)]
    return paths

print('Result (part 1):', len(find_paths('you', 'out')))
