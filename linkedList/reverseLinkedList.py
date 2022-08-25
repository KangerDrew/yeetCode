# My first blind attempt at reverse linked list:

def reverse(head):
    # Edge case - List only consists of one node:
    if not head.next:
        return head

    pre = None

    after = head.next

    return head

