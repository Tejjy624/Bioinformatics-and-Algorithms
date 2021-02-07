import sys

def lcs(p, q):
    n = len(p)
    m = len(q)
    s = []
    b = []
    for i in range(n + 1):
        s.append([])
        b.append([])
        for j in range(m + 1):
            s[-1].append(0)
            b[-1].append(0)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = 0
            if p[i - 1] == q[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                b[i][j] = 'd'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = 'r'
            elif s[i][j] == s[i - 1][j - 1] + match:
                b[i][j] = 'm'
    return b

def backtrack(b, p, i, j):
    if i == 0 or j == 0:
        return ''
    if b[i][j] == 'd':
        return backtrack(b, p, i - 1, j)
    elif b[i][j] == 'r':
        return backtrack(b, p, i, j - 1)
    else:
        return backtrack(b, p, i - 1, j - 1) + p[i - 1]

with open('rosalind_ba5c.txt') as input_file:
    lines = input_file.readlines()

p = lines[0].strip()
q = lines[1].strip()
sys.setrecursionlimit(max(len(p), len(q)) * 2 + 1)
b = lcs(p, q)
print(backtrack(b, p, len(p), len(q)))
