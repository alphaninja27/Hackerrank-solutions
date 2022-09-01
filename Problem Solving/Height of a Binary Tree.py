def height(root):
    if not root:
        return -1
    right = height(root.right)
    left = height(root.left)
    return max(left, right) + 1
