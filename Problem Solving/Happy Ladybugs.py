from collections import Counter
from itertools import groupby

def happyLadybugs(b):
    c = Counter(b)
    if "_" in c:
        c.pop("_")
        if all(v > 1 for v in c.values()):
            return "YES"
        else:
            return "NO"
    else:
        if all(len(list(g)) > 1 for k, g in groupby(b)):
            return "YES"
        else:
            return "NO"
