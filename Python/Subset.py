n = int(input())

for i in range(n):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    out_set = set_a.difference(set_b)
    if len(out_set) == 0:
        print(True)
    else:
        print(False)