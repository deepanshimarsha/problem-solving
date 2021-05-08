class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    reversed = reverseAndClone(head)
    return isEqual(head, reversed)

def reverseAndClone(node):
    head = None
    while node is not None:
        new_node = LinkedListNode(node.data)
        new_node.next = head
        head = new_node
        node = node.next
    return head

def isEqual(one, two):
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next
    return one is None and two is None

a = LinkedListNode(0)
b = LinkedListNode(1)
c = LinkedListNode(2)
d = LinkedListNode(1)
e = LinkedListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

print(isPalindrome(a))
