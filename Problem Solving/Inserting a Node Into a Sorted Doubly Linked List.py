def sortedInsert(head, data):
    # Write your code here
    node=DoublyLinkedListNode(data)
    
    #cas-1 list is empty
    if head==None:
        head=node
    
    #case-2 insert before head
    elif data<head.data:
        node.next=head
        head.prev=node
        head=node
        
    #case-3 insert at speacific position or at the end
    
    else:
        cur=head
    #transerve to specific element.
        while cur.next!=None and cur.data<data:
            cur=cur.next
    
    #insert at the end
        if cur.next==None and cur.data<data:
           cur.next=node
           node.prev=cur
    #insert at specific position
        else:
            previous=cur.prev
        #change previous node
            previous.next=node
            node.prev=previous
        
        #change in current node
            node.next=cur
            cur.prev=node
    return head
