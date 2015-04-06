

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
         
#bfs that includes a start and a finsih for your program

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print ("This is the start to finsih for a BFS of all the fastest possible outcomes for BFS: ", list(bfs_paths(graph, 'A', 'K')))

