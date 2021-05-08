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

    def nodevalue_fromtail(self, position):

        count = 0
        node_value = self.head
        ptr = self.head
        for i in range(0, position+1):
            ptr = ptr.next

        while ptr is not None:
            ptr = ptr.next
            node_value = node_value.next


        print(node_value.data)


if __name__ == "__main__":

    ll1 = LinkedList()

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    ll1.head = node1
    node1.next = node2
    node2.next = node3

    print(ll1)

    ll1.nodevalue_fromtail(0)

