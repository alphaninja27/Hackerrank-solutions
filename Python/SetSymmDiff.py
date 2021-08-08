n1 = int(input())
e = set(input().split())

n2 = int(input())
f = set(input().split())

result = e.union(f) - e.intersection(f)
print(len(result))