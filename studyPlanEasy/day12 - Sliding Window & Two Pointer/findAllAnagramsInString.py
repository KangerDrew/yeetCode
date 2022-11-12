import collections
# New two pointer problem. We initialize a dictionary that keeps track of the letters
# in each substring. We will increment the left and right pointers on the main string s,
# removing and adding the letters using those pointers and checking to see if the
# current substring is an anagram of the input p:


def findAnagrams(s, p):
    # If the length of s is shorter than p, then it's impossible for
    # s to contain any anagram of p in the first place:
    if len(p) > len(s):
        return []

    # Define an array that'll keep track of the indices where the substring
    # is the anagram:
    res = []

    # Define a dictionary that contains the number of letters in the p.
    # We can simply use Counter to do this:
    p_dic = collections.Counter(p)

    # Define a dictionary that will keep track of the substring's letter
    # count. We want our substring to be the same length as p:
    sub_dic = collections.Counter()
    for i in range(len(p)):
        sub_dic[s[i]] += 1

    # Check to see if the first len(p) letters of the input s is the anagram:
    if sub_dic == p_dic:
        res.append(0)

    # Use for loop to add & remove letters from the sub_dic, and while doing so
    # check if the new substring is an anagram or not:
    for right in range(len(p), len(s)):
        left_m1 = right - len(p)

        sub_dic[s[right]] += 1
        sub_dic[s[left_m1]] -= 1

        # Cleaning up. If removal of the string caused the counter to
        # hit zero, we remove that letter from the dictionary:
        if sub_dic[s[left_m1]] == 0:
            sub_dic.pop(s[left_m1])

        if sub_dic == p_dic:
            res.append(left_m1 + 1)

    return res


# print(findAnagrams('cbaebabacd', 'abc'))
print(findAnagrams('bb', 'aa'))
