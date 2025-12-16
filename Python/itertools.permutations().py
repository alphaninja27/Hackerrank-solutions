# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

s, k = input().split()

perm = itertools.permutations(sorted(s), int(k))

for i in perm:
    print("".join(i))
