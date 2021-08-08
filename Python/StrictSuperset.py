a = set(map(int, input().split()))
for x in range(int(input())):
    b = set(map(int, input().split()))
    if len(b.intersection(a))<len(b):
        print("False")
        exit()
print("True")