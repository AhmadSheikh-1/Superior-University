class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def dfs_with_stack(start_node ):
    visited = set( )
    stack = [start_node]

    while stack:
        node= stack.pop()
        if node not in visited:
            print(node.value)  
            visited.add(node)
            
            for neighbor in reversed(node.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')

nodeA.neighbors =[nodeB, nodeC]
nodeB.neighbors = [nodeD, nodeE]

dfs_with_stack(nodeA)
