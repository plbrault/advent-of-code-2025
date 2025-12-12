def parse_input(filename):
    graph = {}
    for line in open(filename).readlines():
        node, neighbours_str = line.replace('\n','').split(': ')
        neighbours = neighbours_str.split(' ')
        graph[node] = neighbours
    return graph

print(parse_input('input.txt'))
