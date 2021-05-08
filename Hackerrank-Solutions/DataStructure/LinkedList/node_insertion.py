class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, head = None):
        self.head = head

    def new_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node

    def push_after(self, position, data):

        new_node = Node(data)
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            if count == position:
                new_node.next = ptr.next
                ptr.next = new_node
            ptr = ptr.next

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

    ll1 = linkedlist()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c

    ll1.head = a
    ll1.push_after(1, 5)


    print(ll1)








