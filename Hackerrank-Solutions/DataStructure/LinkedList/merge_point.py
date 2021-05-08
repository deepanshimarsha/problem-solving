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


    def findMergeNode(self, other):
           ptr1 = self.head
           ptr2 = self.other.head

           while ptr1 != ptr2:

               if ptr1.next is None:
                   ptr1 = self.other.head

               else:
                   ptr1 = ptr1.next

                if ptr2.next is None:
                    ptr2 = self.head

                else:
                    ptr2 = ptr2.next

            return ptr2.data







