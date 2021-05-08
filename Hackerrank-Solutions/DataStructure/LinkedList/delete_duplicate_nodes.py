class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def __str__(self):

        res = ""
        ptr = self.head

        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next

        res = res.strip(", ")

        if len(res):
            return   "[" + res + "]"
        else:
            return "[]"

    def delete_duplicate_node(self):
        ptr1 = self.head
        ptr2 = self.head.next

        while ptr2:
            if ptr1.data != ptr2.data:
                ptr1.next = ptr2
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            else:
                ptr2 = ptr2.next


if __name__ == "__main__":

    ll1 = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(2)
    node5 = Node(3)
    node6 = Node(3)
    node7 = Node(4)
    node8 = Node(5)

    ll1.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node6.next = node7
    node7.next = node8

    print(ll1)
    ll1.delete_duplicate_node()
    print(ll1)