def main(v, w):
    # calculate lcs and return it
    Backtrack = LCSBacktrack(v,w)
    return OutputLCS(Backtrack, v, len(v), len(w))

def LCSBacktrack(v,w):
    s = {}
    Backtrack = {}
    for i in range(len(v)+1):
        s[(i,0)] = 0
    for j in range(len(w)+1):
        s[(0,j)] = 0
    for i in range(len(v)):
        for j in range(len(w)):
            max = s[(i,j+1)]
            direction = '↓'
            m = s[(i+1,j)]
            if m>max:
                max = m
                direction = '→'
            if v[i] == w[j]:
                m = s[(i+1,j+1)]
                if  m>max:
                    max = m
                    direction = '↘'
            s[(i+1, j+1)] = max
            Backtrack[(i+1,j+1)] = direction
    return Backtrack


def OutputLCS(Backtrack, v, i, j):
    if  i==0 or j==0:
        return ""
    if Backtrack[(i,j)] == '↓':
        return OutputLCS(Backtrack,v,i-1,j)
    elif Backtrack[(i,j)] == '→':
        return OutputLCS(Backtrack,v,i,j-1)
    else:
        return OutputLCS(Backtrack,v,i-1,j-1) + v[i-1:i]