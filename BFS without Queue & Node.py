def bfs(graph, start):
    visited = set() 
    current_level = [start]  

    while current_level:
        next_level = [] 
        
        for node in current_level:
            if node not in visited:
                print(node, end= " ")  
                visited.add(node) 
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        next_level.append(neighbor)
        
        current_level = next_level

graph = {
    'A': ['B' , 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')
