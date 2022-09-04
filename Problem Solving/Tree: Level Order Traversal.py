def levelOrder(root):
    #Write your code here
    stack = [root]
    i = 0
    while i < len(stack):
        if stack[i].left:
            stack.append(stack[i].left)
        if stack[i].right:
            stack.append(stack[i].right)
        i += 1
    print(" ".join(str(x) for x in stack))
