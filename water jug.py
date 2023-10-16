print("water jug problem")
def water_jug_problem(capacity_a, capacity_b, target):
    for a in range(capacity_a + 1):
        for b in range(capacity_b + 1):
            if a + b == target:
                return a, b
            if a + b > target and a <= capacity_b and b <= capacity_a:
                return a, b
    return None

capacity_a = 9
capacity_b = 6
target = 0

result = water_jug_problem(capacity_a, capacity_b, target)

if result:
    print(f"Solution found: Jug A = {result[0]}, Jug B = {result[1]}")
else:
    print("Solution not possible.")


    OUTPUT:
        water jug problem
Solution found: Jug A = 0, Jug B = 0




    
