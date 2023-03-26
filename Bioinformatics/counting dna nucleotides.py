def count_symbols(dna_string):
    counts = [0, 0, 0, 0]  # Initialize counts for A, C, G, and T respectively
    for symbol in dna_string:
        if symbol == 'A':
            counts[0] += 1
        elif symbol == 'C':
            counts[1] += 1
        elif symbol == 'G':
            counts[2] += 1
        elif symbol == 'T':
            counts[3] += 1
    return counts
