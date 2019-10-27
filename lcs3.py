def lcs(a, b, c):
    l = [[[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)] for _ in range(len(c) + 1)]
    for i in range(1, len(c) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(a) + 1):
                if a[k - 1] == b[j - 1] == c[i - 1]:
                    l[i][j][k] = 1 + l[i - 1][j - 1][k - 1]
                else:
                    l[i][j][k] = max(l[i - 1][j][k], l[i][j - 1][k], l[i][j][k - 1])
    return l[-1][-1][-1]
