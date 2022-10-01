# Pretty much same problem as top k frequent element:
import heapq

def topKFreqWords(words, k):
    count = {}

    for word in words:
        count[word] = 1 + count.get(word, 0)

    tuple_count = list(count.items())

    # Notice how the lambda function in key uses a tuple.
    # When getting sorted, the nsmallest will return items in order of
    # largest negative frequency (small), then will take lexicographical
    # order of the word into the account:
    unprocessed = heapq.nsmallest(k, tuple_count, key=lambda a: (-a[1], a[0]))

    res = []
    for item in unprocessed:
        res.append(item[0])

    return res
