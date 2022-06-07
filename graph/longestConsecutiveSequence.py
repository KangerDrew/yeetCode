def bruteForceSequence(nums):
    output_max = 0
    # Linear time for looping through nums:
    for num in nums:
        temp_max = 1

        # Since we're looking through an array, we
        while num + 1 in nums:
            temp_max += 1
            num += 1

        output_max = max(temp_max, output_max)

    return output_max


print(bruteForceSequence([100, 4, 200, 1, 3, 2]))
print(bruteForceSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
