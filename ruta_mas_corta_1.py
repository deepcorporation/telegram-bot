def dfs_shortest_path(graph, start, end, path=None, shortest=None):
    if path is None:
        path = []
    path = path + [start]
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    for neighbor in graph[start]:
        if neighbor not in path:
            if shortest is None or len(path) < len(shortest):
                newpath = dfs_shortest_path(graph, neighbor, end, path, shortest)
                if newpath:
                    shortest = newpath
    
    return shortest

grafo = {
    'A': {'B': 5, 'C': 8, 'D': 9},
    'B': {'A': 5, 'E': 15, 'F': 7},
    'C': {'A': 8, 'G': 12, 'H': 10},
    'D': {'A': 9, 'I': 11, 'J': 6},
    'E': {'B': 15, 'K': 9, 'L': 13},
    'F': {'B': 7, 'M': 8, 'N': 6},
    'G': {'C': 12, 'O': 10, 'P': 5},
    'H': {'C': 10, 'Q': 11, 'R': 7},
    'I': {'D': 11, 'S': 14, 'T': 8},
    'J': {'D': 6, 'U': 9, 'V': 12},
    'K': {'E': 9}, 'L': {'E': 13}, 'M': {'F': 8}, 'N': {'F': 6},
    'O': {'G': 10}, 'P': {'G': 5}, 'Q': {'H': 11}, 'R': {'H': 7},
    'S': {'I': 14}, 'T': {'I': 8}, 'U': {'J': 9}, 'V': {'J': 12}
}

start, end = input().split()
path = dfs_shortest_path(grafo, start, end)
if path:
    print(' '.join(path))
else:
    print('None')