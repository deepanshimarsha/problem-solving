#do it iteratively for space efficient solution
def mergeLists(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is not None and head2 is None:
        return head1
    if head1 is None and head2 is not None:
        return head2

    head = None
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    temp = head
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next

    if head1 is None:
        temp.next = head2
    else:
        temp.next = head1

    return head


