# Hello World program in Python

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

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print (dfs(graph, 'A'))           # {'E', 'D', 'F', 'A', 'C', 'B'}
