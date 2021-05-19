class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        ptr1 = head
        ptr2 = ptr1.next
        for i in range(0, n - 1):
            ptr2 = ptr2.next

        if ptr2 is not None:
            while ptr2.next is not None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            ptr1.next = ptr1.next.next
            return head
        else:
            head = ptr1.next
            ptr1.next = None
            return head
