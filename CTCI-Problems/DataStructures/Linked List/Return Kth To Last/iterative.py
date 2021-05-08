#time complexity - O(n)
#space - O(1)

def KthNode(head, k):
    ptr1 = head
    ptr2 = head.next
    for i in range(k):
        if ptr2 is None:
            return None
        ptr2 = ptr2.next

    while ptr1 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1.val