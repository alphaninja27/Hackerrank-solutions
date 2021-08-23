n = int(input())
x = [float(i) for i in input().strip().split()]
y = [float(i) for i in input().strip().split()]

rx = [sorted(x).index(i) for i in x]
ry = [sorted(y).index(i) for i in y]

rxy =1-(sum([(rx[i]-ry[i])**2 for i in range(n)])*6/(n*(n**2-1)))
print(round(rxy,3))