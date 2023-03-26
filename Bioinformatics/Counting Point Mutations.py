def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("s and t must be of equal length.")
    return sum(1 for x, y in zip(s, t) if x != y)
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
print(hamming_distance(s, t)) # Output: 7
