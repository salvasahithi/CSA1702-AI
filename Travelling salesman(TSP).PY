import sys
def nearest_neighbor(graph, start):
    visited = [False] * len(graph)
    visited[start] = True
    path = [start]
    total_distance = 0
    for _ in range(len(graph) - 1):
        min_distance = sys.maxsize
        nearest_city = None
        for i in range(len(graph)):
            if not visited[i] and graph[path[-1]][i] < min_distance:
                min_distance = graph[path[-1]][i]
                nearest_city = i
        path.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance
    total_distance += graph[path[-1]][start]
    path.append(start)
    return path, total_distance

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0
path, distance = nearest_neighbor(graph, start_city)

print(f"Optimal Path: {path}")
print(f"Total Distance: {distance}")
