def mergeLists(head1, head2):
    dummy = SinglyLinkedList()
    tail = dummy
    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2= head2.next
        tail = tail.next
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2
    return dummy.next
