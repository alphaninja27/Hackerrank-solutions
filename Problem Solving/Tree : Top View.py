def topView(root):
    #Write your code here
    res_map = {}
    queue = []
    queue.append((root, 0))
    while queue:
        node, pos = queue.pop(0)
        if pos not in res_map:
            res_map[pos] = node.info
        if node.left:
            queue.append((node.left, pos-1))
        if node.right:
            queue.append((node.right, pos+1))
