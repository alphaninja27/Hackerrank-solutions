def findMergeNode(head1, head2):
    while head1:
        head1.data = str(head1.data) + "v"
        head1 = head1.next
    while head2:
        if str(head2.data)[-1] == "v":
            return int(head2.data[:-1])
        head2 = head2.next
