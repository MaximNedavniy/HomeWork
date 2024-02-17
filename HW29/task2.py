def bfs_shortest_paths(graph, start):
    paths = {}
    for node in graph:
        paths[node] = {'path': [], 'distance': float('inf')}

    paths[start] = {'path': [start], 'distance': 0}

    queue = [start]
    front = 0

    while front < len(queue):
        current_node = queue[front]
        front += 1
        current_distance = paths[current_node]['distance']

        for neighbor in graph[current_node]:
            if paths[neighbor]['distance'] == float('inf'):
                queue.append(neighbor)
                paths[neighbor]['distance'] = current_distance + 1
                paths[neighbor]['path'] = paths[current_node]['path'] + [neighbor]

    return paths

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

all_shortest_paths = {}
for node in graph:
    all_shortest_paths[node] = bfs_shortest_paths(graph, node)

print("Shortest paths from each vertex to every other vertex:")
for node in all_shortest_paths:
    print(f"From vertex {node}:")
    for target, path_data in all_shortest_paths[node].items():
        if node != target:
            print(f"To vertex {target}: {' -> '.join(path_data['path'])}, Distance: {path_data['distance']}")
