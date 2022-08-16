class MinHeap:

    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        # if getParentIndex returns a negative number, it means
        # that the provided index cannot have a parent!
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        # If the left child index is less than the size of the heap,
        # then the current index should have a left child.
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        # If the right child index is less than the size of the heap,
        # then the current index should have a right child.
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    # # Iterative heapifyUp and insert methods:
    # def heapifyUp(self):
    #
    #     index = self.size - 1
    #     while self.hasParent(index) and self.parent(index) > self.storage[index]:
    #         self.swap(self.getParentIndex(index), index)
    #
    # def insert(self, data):
    #
    #     if self.isFull():
    #         raise "Heap is Full"
    #
    #     self.storage[self.size] = data
    #     self.size += 1
    #     self.heapifyUp()

    def heapifyUp(self, index):
        if self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def insert(self, data):
        if self.isFull():
            raise "Heap is Full"

        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    # # Iterative heapifyDown and removeMin methods:
    # def heapifyDown(self):
    #     # start from the root
    #     index = 0
    #     # Use while loop, and at the beginning check that the left child.
    #     # This is because the heap must be a complete tree, thus it must be
    #     # filled from left from right!
    #     while self.hasLeftChild(index):
    #         # Temporarily smallerChildIndex variable, and set it as left child index
    #         smallerChildIndex = self.getLeftChildIndex(index)
    #         # Then, we check if there is a right child, and whether the value is greater
    #         # or less than the right child:
    #         if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
    #             smallerChildIndex = self.getRightChildIndex(index)
    #
    #         # Now, check if the current node we're at is smaller than the two of its children.
    #         # If true, we no longer need to heapify down, so break.
    #         if self.storage[index] < self.storage[smallerChildIndex]:
    #             break
    #         # otherwise, we need to swap the smallest child and the parent and continue
    #         else:
    #             self.swap(index, smallerChildIndex)
    #         # Update the index to smallerChildIndex
    #         index = smallerChildIndex
    #
    # def removeMin(self):
    #     if self.size == 0:
    #         raise "Empty Heap"
    #
    #     data = self.storage[0]
    #     # Place the largest (last element) at the root. We will
    #     # heapify this element down to make our heap valid again!
    #     self.storage[0] = self.storage[self.size - 1]
    #     self.size -= 1
    #     self.heapifyDown()
    #
    #     return data

    def heapifyDown(self, index):
        # Tentatively name the current index we're on as "smallest"
        smallest = index

        # Check the left value against the smallest (index) value
        if self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)
        # Check the right value against the smallest value (after checking left)
        if self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index):
            smallest = self.getRightChildIndex(index)

        # If smallest value was not changed by the above two if conditions, we don't need
        # to recurse down. Otherwise, we swap the smallest element w current element, and
        # continue to heapify down.
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)

    def removeMin(self):
        if self.size == 0:
            raise "Empty Heap"

        data = self.storage[0]
        # Place the largest (last element) at the root. We will
        # heapify this element down to make our heap valid again!
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)

        return data
