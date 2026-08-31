# Part 1
def flatten_and_filter(matrix):
    """ Takes a list of lists containing integers """
    results = []
    for row in matrix:
        for num in row:
            if num % 2 == 0:
                results.append(num**3)
    return results

# Part 2
def collatz_steps(n):
    """Keep track of how many total steps (iterations) it takes to reach 1, and return that count."""
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Part 3
def nucleotide_count(sequence):
    """Iterate through the string and populate a dictionary counting the occurrences of each character."""
    sequence = sequence.lower()
    counts = {}
    for char in sequence:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# Part 4
def compare_enrollments(roster_a, roster_b):
    """Convert the two input lists into Python `set` objects."""
    combined_set = {}
    roster_a_set = set(roster_a)
    roster_b_set = set(roster_b)
    combined_set["both"] = roster_a_set.intersection(roster_b_set)
    combined_set["only_a"] = roster_a_set.difference(roster_b_set)
    combined_set["only_b"] = roster_b_set.difference(roster_a_set)
    combined_set["all_unique"] = roster_a_set.union(roster_b_set)
    return combined_set

print(flatten_and_filter([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(collatz_steps(1001))
print(nucleotide_count("ATCGATCG"))
print(compare_enrollments(["Alice", "Bob", "Charlie"], ["Bob", "Charlie", "David"]))