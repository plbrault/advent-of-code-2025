graph = {}
for line in open('input.txt').readlines():
    node, neighbours_str = line.replace('\n','').split(': ')
    neighbours = neighbours_str.split(' ')
    graph[node] = neighbours

def solve_part1():
    def find_paths_to_out(node):
        num_paths_to_out = 0
        for neighbour in graph[node]:
            if neighbour == 'out':
                return 1
            else:
                num_paths_to_out += find_paths_to_out(neighbour)
        return num_paths_to_out
    
    print('Result (part 1):', find_paths_to_out('you'))

solve_part1()
