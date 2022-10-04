# Simplest solution is to just append every value of the list to an array, and
# increment from left and right towards the center to check if every value match:

# However, this solution costs O(n) memory. This isn't the most ideal solution...
def palindromeLLEasy(head):

    travelled = []

    while head:
        travelled.append(head.val)
        head = head.next

    left, right = 0, len(travelled) - 1

    while left < right:
        if travelled[left] != travelled[right]:
            return False

        left += 1
        right -= 1

    return True


