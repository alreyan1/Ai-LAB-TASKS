def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        word = stack.pop()
        if word not in visited:
            print(word, end=" ")
            visited.add(word)
            for neighbor in reversed(graph[word]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

dfs_stack(graph, 'A')
