def is_valid(node, color, coloring, graph):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def map_coloring(node, colors, coloring, graph):
    if node == len(graph):
        return coloring

    for color in colors:
        if is_valid(node, color, coloring, graph):
            coloring[node] = color
            result = map_coloring(node + 1, colors, coloring, graph)
            if result:
                return result
            coloring[node] = None

    return None

graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}

colors = ['Red', 'Green', 'Blue']

coloring = [None] * len(graph)
solution = map_coloring(0, colors, coloring, graph)

if solution:
    for node, color in solution.items():
        print(f"Node {node} is colored {color}")
else:
    print("No solution found.")
