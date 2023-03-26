def fibonacci(n, m):
    # initialize the sequence with 1 pair of rabbits at month 0 and 1
    seq = [1, 1]
    for i in range(2, n):
        # each month, rabbits older than m months die and the rest reproduce
        if i < m:
            seq.append(seq[-1] + seq[-2])
        elif i == m or i == m+1:
            seq.append(seq[-1] + seq[-2] - 1)
        else:
            seq.append(seq[-1] + seq[-2] - seq[i-m-1])
    return seq[-1]

n = 84
m = 18
print(fibonacci(n, m))
