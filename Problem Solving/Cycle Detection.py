def has_cycle(head):
    if not head:
        return 0
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        while slow == fast:
            return 1
    return 0
