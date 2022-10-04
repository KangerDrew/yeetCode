# My first blind attempt solution. Passed!
def oddEvenLinkedListBlind(head):
    if not head:
        return head

    odd_list = head
    even_list = head.next
    even_head = even_list

    while even_list and even_list.next:
        odd_list.next = odd_list.next.next
        even_list.next = even_list.next.next

        odd_list = odd_list.next
        even_list = even_list.next

    odd_list.next = even_head

    return head
