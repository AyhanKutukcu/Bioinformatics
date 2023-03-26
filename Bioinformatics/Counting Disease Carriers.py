def calc_hwe_probs(A):
    # Calculate the proportion of homozygous recessive individuals for each factor
    # and use it to calculate the proportion of homozygous dominant and heterozygous individuals
    p = [(1 - (A[i] ** 0.5)) for i in range(len(A))]

    # Calculate the frequency of the recessive allele for each factor
    q = [(1 - pi) for pi in p]

    # Calculate the probability of carrying at least one copy of the recessive allele
    # for each factor
    B = [1 - (q[i] ** 2) for i in range(len(q))]

    return B
A = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
B = calc_hwe_probs(A)
print(B)
