def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    if llist is not None:
        node.next = llist
    return node
