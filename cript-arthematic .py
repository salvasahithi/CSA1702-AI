print("cryptarthimetic")
def is_solution_valid(mapping, words, result):
    word_values = [int(''.join(str(mapping[c]) for c in word)) for word in words]
    result_value = int(''.join(str(mapping[c]) for c in result))

    return sum(word_values) == result_value

def solve_cryptarithmetic(words, result):
    all_letters = set(''.join(words + [result]))
    if len(all_letters) > 10:
        return None  
    unique_letters = sorted(all_letters)
    permutations = range(10)  

    from itertools import permutations as permute
    for perm in permute(permutations, len(unique_letters)):
        mapping = {letter: digit for letter, digit in zip(unique_letters, perm)}
        if mapping[result[0]] == 0:  
            continue
        if is_solution_valid(mapping, words, result):
            return mapping

    return None  
print("SEND + MORE = MONKEY")
words = ['send', 'more']
result = 'monkey'

solution = solve_cryptarithmetic(words, result)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print("No solution found for the given cryptarithmetic problem.")


    OUTPUT:
        cryptarthimetic
SEND + MORE = MONKEY
No solution found for the given cryptarithmetic problem.
