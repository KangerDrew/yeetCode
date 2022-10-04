# My first blind attempt solution. Passed!
def oddEvenLinkedListBlind(head):
    if not head:
        return head

    # Initially, I wrote a different if statement to cover the cases
    # where linked list length is 1 or 2. For those scenarios, we don't
    # need to make any changes to the list at all, so return back the head:
    # if not head or not head.next or head.next.next:
    #     return head

    # If none of the above were true, we need to initialize 3 pointers. Two
    # for traversing the odd numbered nodes and even number nodes, and a third
    # pointer to keep track of where the "head" of the even numbered node is:
    odd_list = head
    even_list = head.next
    even_head = even_list

    # The while loop below will use the odd_list and even_list pointer to reset
    # the .next pointer of their each respective node to jump by 2x steps. This
    # makes it so that all the "odd" nodes are pointing after another, and all
    # the "even" nodes point after another.
    while even_list and even_list.next:
        odd_list.next = odd_list.next.next
        # The above line "odd_list.next = odd_list.next.next" will NOT affect the
        # setting the even nodes. At the moment, the even.next is only 1 node length
        # away from the current node. running "even_list.next = even_list.next.next
        # will set the pointer to a node 2 node length away:
        even_list.next = even_list.next.next

        # Move the two pointer forward, they'll be in position for next odd & even:
        odd_list = odd_list.next
        even_list = even_list.next

    # Once all the pointers have been modified, use the stored reference to the
    # starting point (head) of the even list and set that to be the next of the
    # current odd_list pointer. The odd_list pointer should be at the end of its
    # own list:
    odd_list.next = even_head

    # All the pointers have been modified. Return the head back:
    return head


# Explanations in the code may not be clear... It's much easier if you draw
# it out on the board to see how each loop alters the original list...
