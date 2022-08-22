def preOrder(root):
    #Write your code here
    if root is None:
        return

    node_stack = []
    node_stack.append(root)

    while len(node_stack) > 0:

        root = node_stack.pop()
        print(root, end = " ")

        if root.right:
            node_stack.append(root.right)

        if root.left:
            node_stack.append(root.left)
