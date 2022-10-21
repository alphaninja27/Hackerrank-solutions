def insertNodeAtPosition(llist, data, position):
    # Write your code here
    current = llist  # Initialise temp
    count = 0  # Index of current node
 
    # Loop while end of linked list is not reached
    while (current):
        if (count == position-1):
            new_node = SinglyLinkedListNode(data)
            new_node.next = current.next
            current.next = new_node
        count += 1
        current = current.next
    return llist
