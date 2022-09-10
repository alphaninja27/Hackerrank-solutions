prev = None
def check_binary_search_tree_(root):
    global prev
    if root:
        if not check_binary_search_tree_(root.left):
            return False
        if prev!=None and root.data <= prev:
            return False
        prev=root.data
        return check_binary_search_tree_(root.right)
    else:
        return True
