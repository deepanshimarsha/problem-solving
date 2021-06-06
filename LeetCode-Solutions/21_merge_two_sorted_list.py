class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        if ptr1 is None and ptr2 is not None:
            return ptr2
        if ptr2 is None and ptr1 is not None:
            return ptr1

        if ptr1 is not None and ptr2 is not None:
            if ptr1.val >= ptr2.val:
                head = ptr2
                ptr2 = ptr2.next
            else:
                head = ptr1
                ptr1 = ptr1.next

            prev = head
            while ptr1 is not None and ptr2 is not None:

                if ptr1.val >= ptr2.val:
                    prev.next = ptr2
                    prev = ptr2
                    ptr2 = ptr2.next
                else:
                    prev.next = ptr1
                    prev = ptr1
                    ptr1 = ptr1.next

            if ptr2 is None:
                while ptr1 is not None:
                    prev.next = ptr1
                    prev = ptr1
                    ptr1 = ptr1.next

            if ptr1 is None:
                while ptr2 is not None:
                    prev.next = ptr2
                    prev = ptr2
                    ptr2 = ptr2.next
            return head
