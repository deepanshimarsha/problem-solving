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

    def cycle_detection(self):
        if self.head is None:
            return 0

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return 1

        return 0



if __name__ == "__main__":

    ll1 = LinkedList()

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    ll1.head = node1
    node1.next = node2
    node2.next = node3


    print(ll1)
    print(ll1.cycle_detection())
    print(ll1)