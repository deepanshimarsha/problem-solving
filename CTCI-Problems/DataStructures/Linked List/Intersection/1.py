#time complexity - O(l1+l2)
#space complexity - O(1)

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def Intersection(head1, head2):

    #get tail and size of linked list
    ptr1 = head1
    ptr2 = head2
    l1 = 0
    l2 = 0
    while ptr1.next is not None:
        l1 += 1
        ptr1 = ptr1.next

    while ptr2.next is not None:
        l2 += 1
        ptr2 = ptr2.next

    #compare the tails
    if ptr1 != ptr2:
        return None

    #difference in length
    diff = abs(l1-l2)


    #set pointers for the linkedlists
    if l1 > l2:
        longer = head1
        shorter = head2
    else:
        longer = head2
        shorter = head1
    longer = MoveLonger(longer, diff)

    #traverse until they are pointing at same node
    while longer != shorter:
        longer = longer.next
        shorter = shorter.next
    return longer.data


def MoveLonger(pointer, diff):
    for i in range(diff):
        pointer = pointer.next
    return pointer

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)
f = LinkedListNode(6)
g = LinkedListNode(7)
a.next = b
b.next = c
c.next = f
f.next = g
d.next = e
e.next = f

print(Intersection(a, d))









