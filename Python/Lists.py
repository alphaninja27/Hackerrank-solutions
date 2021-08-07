if __name__ == '__main__':
    L=[]
    n = int(input())
for i in range(n):
    y = input()
    
    temp = y.split(" ")
    if temp[0] == 'append':
        L.append(int(temp[1]))
    elif temp[0] == 'sort':
        L= sorted(L)
    elif temp[0] == 'pop':
        L.pop()
    elif temp[0] == 'remove':
        L.pop(L.index(int(temp[1])))
    elif temp[0] == 'reverse':
        L.reverse()
    elif temp[0] == 'insert':
        L.insert(int(temp[1]),int(temp[2]))
    else:
        print(L)