class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ptr1 = l1
        ptr2 = l2

        add = ptr1.val + ptr2.val + carry
        if add not in range(0, 10):
            carry = add // 10
            l3 = ListNode(add % 10)
        else:
            carry = 0
            l3 = ListNode(add)

        ptr1 = ptr1.next
        ptr2 = ptr2.next
        ptr3 = l3

        while ptr1 is not None or ptr2 is not None:
            if ptr1 is None or ptr2 is None:
                break

            add = ptr1.val + ptr2.val + carry
            if add not in range(0, 10):
                carry = add // 10
                new_node = ListNode(add % 10)
            else:
                carry = 0
                new_node = ListNode(add)
            ptr3.next = new_node
            ptr3 = new_node
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr1 is None:
            while ptr2 is not None:
                add = ptr2.val + carry
                if add not in range(0, 10):
                    carry = add // 10
                    new_node = ListNode(add % 10)
                else:
                    carry = 0
                    new_node = ListNode(add)
                ptr3.next = new_node
                ptr3 = new_node
                ptr2 = ptr2.next

            if carry != 0:
                new_node = ListNode(carry)
                ptr3.next = new_node

        if ptr2 is None:
            while ptr1 is not None:
                add = ptr1.val + carry
                if add not in range(0, 10):
                    carry = add // 10
                    new_node = ListNode(add % 10)
                else:
                    carry = 0
                    new_node = ListNode(add)
                ptr3.next = new_node
                ptr3 = new_node
                ptr1 = ptr1.next
            if carry != 0:
                new_node = ListNode(carry)
                ptr3.next = new_node

        return l3

