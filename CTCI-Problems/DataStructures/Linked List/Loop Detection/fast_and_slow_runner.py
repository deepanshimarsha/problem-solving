def LoopDetection(head):
    fast = head
    slow = head

    #move fast at 2 step rate and slow at 1 step rate
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    #no loop found
    if fast is None or fast.next is None:
        return None

    #find loop start node
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast