#time complexity - O(n)
#uses extra space - O(1)
def RemoveDups(head):
    n = head
    previous = None
    seen = set()
    while n != None:
        if n.val is in seen:
            previous.next = n.next
        else:
            seen.add(n.val)
            previous = n
        n = n.next
    return head

