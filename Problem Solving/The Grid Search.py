for row in range(len(G) - len(P) + 1):
        for col in range(len(G[0]) - len(P[0]) + 1):
            for i in range(len(P)):
                if P[i] != G[row + i][col : col + len(P[0])]:
                    found = 'NO'
                    break
                else:
                    found = 'YES'
            if found == 'YES':
                return found
    return found
