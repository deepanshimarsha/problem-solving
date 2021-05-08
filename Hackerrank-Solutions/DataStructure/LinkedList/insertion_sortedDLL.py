class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head=None):
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

    def insertion_sorted_list(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node

        else:
            ptr = self.head

            while ptr.next and ptr.next.data < new_node.data:
                ptr = ptr.next

            new_node.next = ptr.next
            if ptr.next is not None:
                new_node.next.prev = new_node

            ptr.next = new_node
            new_node.prev = ptr












if __name__ == "__main__":

    ll1 = LinkedList()

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    ll1.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2


    print(ll1)

    ll1.insertion_sorted_list(15)

    print(ll1)
