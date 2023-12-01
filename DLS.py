def depth_limited_search(graph, start, goal, max_depth, path=None):
    if path is None:
        path = [start]

    if start == goal:
        return path

    if max_depth <= 0:
        return None

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = depth_limited_search(graph, node, goal, max_depth - 1, path + [node])
            if new_path:
                return new_path

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'
maximum_depth = 3

result = depth_limited_search(graph, start_node, goal_node, maximum_depth)

if result:
    print(f"Path from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found within depth {maximum_depth}")
