node = llist
    while node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return llist
