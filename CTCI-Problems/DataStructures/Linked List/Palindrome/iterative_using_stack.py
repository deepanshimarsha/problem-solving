def isPalindrome(head):
    slow = head
    fast = head
    stach = []

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    #if linked list length is odd
    if fast is not None:
        #ignore the middle element
        slow = slow.next

    while slow is not None:
        top = stack.pop
        if top.data != slow.data:
            return False
        slow = slow.next
    return True

