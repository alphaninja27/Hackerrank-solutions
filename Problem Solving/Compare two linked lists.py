def compare_lists(llist1, llist2):
    if llist1 is None and llist2 is None:
        return 1
    if llist1 is None or llist2 is None:
        return 0
    if llist1.data != llist2.data:
        return 0
    return compare_lists(llist1.next,llist2.next)
