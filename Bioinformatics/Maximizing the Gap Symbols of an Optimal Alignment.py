def max_gap_symbols(s, t, m, d, g):
    N, M = len(s), len(t)
    S = [[m if s[i] == t[j] else d for j in range(M)] for i in range(N)]
    P = [g] * (max(N, M) + 1)
    D = [[0] * (M+1) for _ in range(N+1)]
    G = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        D[i][0] = i * P[1]
        G[i][0] = i
    for j in range(1, M+1):
        D[0][j] = j * P[1]
        G[0][j] = j
    for i in range(1, N+1):
        for j in range(1, M+1):
            D[i][j] = max(D[i-1][j-1] + S[i-1][j-1],
                          D[i-1][j] + P[1],
                          D[i][j-1
