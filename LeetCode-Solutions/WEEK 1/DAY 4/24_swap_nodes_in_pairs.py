class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        lists = []
        if head is None:
            return
        if head.next is None:
            return head
        ptr1 = head
        j = -2
        while ptr1 != None:
            lists.append(ptr1.val)
            ptr1 = ptr1.next

        for i in range(0, len(lists)):
            i = j + 2
            if i > len(lists) - 2:
                break
            lists[i], lists[i + 1] = lists[i + 1], lists[i]
            # print(lists[i])

            j = i
        head = ListNode(lists[0])
        ptr = head
        for i in range(1, len(lists)):
            new_node = ListNode(lists[i])
            ptr.next = new_node
            ptr = new_node
        return head

