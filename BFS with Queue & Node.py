class Node:
    def __init__(self, value):
        self.value = value

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

def bfs_with_queue_and_node(graph, start):
    visited = set()
    queue = Queue()
    queue.enqueue(Node(start))

    while not queue.is_empty():
        node = queue.dequeue()
        if node.value not in visited:
            print(node.value, end=" ")
            visited.add(node.value)

            for neighbor in graph[node.value]:
                if neighbor not in visited:
                    queue.enqueue(Node(neighbor))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs_with_queue_and_node(graph, 'A')
