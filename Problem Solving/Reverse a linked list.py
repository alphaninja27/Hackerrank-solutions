def reverse(llist):
    # Write your code here
    prev, curr = None, llist
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp        
    return prev
