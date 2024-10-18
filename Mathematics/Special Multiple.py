def solve(n):
    # Write your code here
    q = ['9']
    while q:
        curr = q.pop(0)
        if int(curr) % n == 0:
            return curr
        q.append(curr + '0')
        q.append(curr + '9')
