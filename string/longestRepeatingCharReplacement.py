def charReplacementFast(s, k):
    letters = {}
    left = 0
    most_common_letter_count = 0

    longest_sub = 0

    for right in range(len(s)):

        if s[right] not in letters:
            letters[s[right]] = 1
        else:
            letters[s[right]] += 1

        most_common_letter_count = max(most_common_letter_count, letters[s[right]])

        while (right + 1 - left - most_common_letter_count) > k:
            letters[s[left]] -= 1
            left += 1

        longest_sub = max(right + 1 - left, longest_sub)

    return longest_sub

