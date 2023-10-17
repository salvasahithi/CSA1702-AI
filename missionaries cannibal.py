from queue import Queue
initial_state = (3, 3, 1)  # (M, C, B) on the starting side
goal_state = (0, 0, 0)  # (M, C, B) on the ending side

def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3 or (m != 0 and m < c) or (m != 3 and m > c):
        return False
    return True

def get_neighbors(state):
    m, c, b = state
    neighbors = []
    if b == 1:
        for i in range(1, 3):
            new_state = (m - i, c, 0)
            if is_valid(new_state):
                neighbors.append(new_state)
            new_state = (m, c - i, 0)
            if is_valid(new_state):
                neighbors.append(new_state)
    else:
        new_state = (m + 1, c, 1)
        if is_valid(new_state):
            neighbors.append(new_state)
        new_state = (m, c + 1, 1)
        if is_valid(new_state):
            neighbors.append(new_state)
        new_state = (m + 1, c + 1, 1)
        if is_valid(new_state):
            neighbors.append(new_state)
    return neighbors

def bfs():
    visited = set()
    q = Queue()
    q.put((initial_state, []))

    while not q.empty():
        current_state, path = q.get()
        if current_state == goal_state:
            return path
        if current_state in visited:
            continue
        visited.add(current_state)

        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                q.put((neighbor, new_path))

    return None

def print_solution(path):
    for i, state in enumerate(path):
        m, c, b = state
        print(f"Step {i+1}: ({m}M, {c}C, {b}B)")

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")
