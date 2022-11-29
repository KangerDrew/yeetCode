import collections

arr = [1, 2, 3]
new_arr = collections.deque(arr)
print(new_arr)
print(len(new_arr))
new_arr.popleft()
new_arr.popleft()
print(len(new_arr))