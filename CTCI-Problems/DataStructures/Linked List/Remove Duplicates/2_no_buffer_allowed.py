#time complexity - O(n^2)
#no extra space
def RemoveDups(head):
    current = head
    while current != None:
        runner = current
        while runner != None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next