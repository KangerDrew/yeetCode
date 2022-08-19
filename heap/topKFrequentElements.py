from collections import Counter, defaultdict

# IMPORTANT: In questions where we are looking for a top k elements
# that satisfy a certain condition, it is often a good idea to think about
# using heaps!


# The idea is to use min-heap to store the frequency of the integer. By keeping
# the size of the heap as k, the min-heap will keep track of the k most frequent
# counts.


test = [1, 1, 1, 2, 2, 3]
count = Counter(test)
print(count)

other_count = defaultdict(int)
other_count["a"] += 1
other_count["b"] += 4
print(other_count)
print(other_count["b"])
