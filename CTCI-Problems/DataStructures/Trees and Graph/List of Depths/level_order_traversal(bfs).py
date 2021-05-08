#iterative approach
#time complexity - O(n)
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ListofDepths(root):
    q = []
    if root is not None:
        head = LinkedListNode(root.value)
        ptr1 = head
        q.append(root)

    while len(q) > 0:
        poped_item = q.pop(0)

        if poped_item.left:
            node = LinkedListNode(poped_item.left.value)
            ptr1.next = node
            ptr1 = node
            q.append(poped_item.left)
        if poped_item.right:
            node = LinkedListNode(poped_item.right.value)
            ptr1.next = node
            ptr1 = node
            q.append(poped_item.right)

    return head

def printLinkedList(head):
    ptr = head
    while ptr is not None:
        print(ptr.value)
        ptr = ptr.next


root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d
printLinkedList(ListofDepths(root))




