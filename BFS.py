from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])  
    
    while queue:
        node = queue.popleft()  
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            

            queue.extend(graph[node])


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


bfs(graph, 'A')
