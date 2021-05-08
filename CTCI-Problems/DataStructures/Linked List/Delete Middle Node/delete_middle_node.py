#you are not given access to the head of the linked list
#you only have access to a middle node
#copy data from the next node over to the current node
#then delete the next node
def DeleteNode(n):
    #n = linked list node
    if n is None or n.next is None:
        return False
    next = n.next
    n.data = next.data
    n.next = next.next
    return True

