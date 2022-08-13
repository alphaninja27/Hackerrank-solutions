n = int(input())

# myString = Solution()
s = ""
stack = []

for i in range(n):
    t = input().split()
    if(int(t[0]) == 1):
        stack.append(s)
        s += t[1]
        
    elif(int(t[0]) == 2):
        stack.append(s)
        s = s[:(len(s)-int(t[1]))]
        
    elif(int(t[0]) == 3):
        print(s[int(t[1])-1])
        
    else:
        s = stack.pop()
