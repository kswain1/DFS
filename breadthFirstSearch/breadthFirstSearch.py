graph = {'A': set(['B','E',]),
         'B': set(['A','C', 'F']),
         'C': set(['B','G']),
         'D': set(['H','L']),
         'E': set(['A','I', 'F']),
         'F': set(['E','J', 'K']),
         'G': set(['C','K']),
         'H': set(['D','L']),
         'I': set(['E','J']),
         'J': set(['F','I']),
         'K': set(['G','F'])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))
