def lcs(a, b):
    l = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
    for i in range(len(a) + 1):
        l[0][i] = 0
    for i in range(len(b) + 1):
        l[i][0] = 0
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[j-1] == b[i-1]:
                l[i][j] = 1 + l[i - 1][j - 1]
            else:
                l[i][j] = max(l[i - 1][j], l[i][j-1])
    return l[-1][-1]

