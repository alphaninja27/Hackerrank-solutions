def sequence(N):
    x = N % 8
    if x == 0 or x == 1:
        return N
    if x == 2 or x == 3:
        return 2
    if x == 4 or x == 5:
        return N+2
    if x == 6 or x == 7:
        return 0

def xorSequence(l, r):
    return sequence(r) ^ sequence(l-1)
