count =0
    temp = llist
    if position == 0:
        llist = llist.next 
    while temp.next:
        if count == position -1:
            temp.next = temp.next.next
        count+=1
        temp = temp.next
    return llist
