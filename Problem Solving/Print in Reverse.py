def reversePrint(llist):
    # Write your code here
    if llist is None:
        return
    reversePrint(llist.next)
    print(llist.data)
        
