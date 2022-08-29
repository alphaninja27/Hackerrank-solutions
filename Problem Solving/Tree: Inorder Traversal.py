def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(root,end=" ")
        inOrder(root.right)
