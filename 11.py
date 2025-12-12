graph = {}
for line in open('input.txt').readlines():
    node, neighbours_str = line.replace('\n','').split(': ')
    neighbours = neighbours_str.split(' ')
    graph[node] = neighbours

memo = {}

def find_paths(start, end, *, must_contain=[]):
    print(start)
    if (start, end) in memo:
        return memo[(start, end)]

    paths = []
    if start not in graph:
        return paths
    for neighbour in graph[start]:
        if neighbour == end:
            paths.append([start, end])
        else:
            new_paths = [([start] + path) for path in find_paths(neighbour, end)]
            for path in new_paths:
                is_valid = True
                for node in must_contain:
                    if node not in path:
                        is_valid = False
                        break
                if is_valid:
                    paths.append(path)

    memo[(start, end)] = paths
    return paths

print('Result (part 1):', len(find_paths('you', 'out')))

print(len(find_paths('svr', 'out', must_contain=['dac', 'fft'])))
