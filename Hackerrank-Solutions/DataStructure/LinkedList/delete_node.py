class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
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
            return "[" + res + "]"
        else:
            return "[]"
    def delete_node_after(self,position):

        ptr1 = self.head
        ptr2 = self.head.next
        for i in range(1, position):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr2 == None:
            return print("position out of range")

        ptr1.next = ptr2.next


if __name__ == "__main__":
    ll1 = linkedlist()

    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    ll1.head = a
    print(ll1)

    ll1.delete_node_after(5)

    print(ll1)

