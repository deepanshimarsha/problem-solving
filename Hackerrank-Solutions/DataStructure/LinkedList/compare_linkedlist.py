class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head


    def compare_lists(self, llist2):
        ptr1 = self.head
        ptr2 = llist2.head
        while ptr1 is not None and ptr2 is not None and ptr1.data == ptr2.data:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1 == ptr2



    def __str__(self):

        res = ""
        ptr = self.head

        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next

        res = res.strip(", ")

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


if __name__ == "__main__":

    ll1 = LinkedList()

    node1 = Node(1)
    node2 = Node(2)



    ll1.head = node1
    node1.next = node2


    ll2 = LinkedList()

    a = Node(1)
    b = Node(2)



    ll2.head = a
    a.next = b

    print(ll1)
    print(ll2)

    print(ll1.compare_lists(ll2))

