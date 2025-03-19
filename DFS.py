def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)


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

dfs(graph, 'A')
