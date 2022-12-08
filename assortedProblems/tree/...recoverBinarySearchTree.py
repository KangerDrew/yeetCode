

def find_two_swapped(nums):

    n1 = n2 = None

    for i in range(len(nums) - 1):

        if nums[i + 1] < nums[i]:
            n2 = nums[i + 1]

            if n1 is None:
                n1 = nums[i]
            else:
                break

    return n1, n2


print(find_two_swapped([3, 2, 1]))
print(find_two_swapped([1, 2, 7, 4, 5, 6, 3, 8]))
