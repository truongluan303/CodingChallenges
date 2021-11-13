
def has_cycle(graph: dict) -> bool:

    path = set()

    def visit(vertex):
        path.add(vertex)

        for neighbor in graph.get(vertex, ()):
            if neighbor in path or visit(neighbor):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in graph)

    



def get_reversed_graph(graph: dict) -> dict:
        
    rev_graph = dict()

    for vertex in graph:
        rev_graph[vertex] = list()

    for vertex in graph:
        for neighbor in graph[vertex]:
            rev_graph[neighbor].append(vertex)

    return rev_graph





def main():
    
    graph = dict()

    print('\nEnter the adjacency list for the graph:')
    while True:
        line = input().strip()

        if line == '':
            break

        key, val = line.split(':')
        neighbors = val.split()

        graph[key] = neighbors

    print('----------------------------------------\n')

    is_cyclic = has_cycle(graph)
    graph_type = 'CYCLIC' if is_cyclic else 'ACYCLIC'
    print('CONTAINS CYCLE:', is_cyclic, '==>', graph_type)

    rev_graph = get_reversed_graph(graph)

    print('\n\nREVERSED GRAPH:\n')
    for vertex, neighbors in rev_graph.items():
        print(vertex, ':', neighbors)

    print()

        




if __name__ == '__main__':
    main()