import random


# My attempt following the mock interview:
class RandomizedSet:

    def __init__(self):
        self.content = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:

        if val in self.indexMap:
            return False

        self.content.append(val)
        self.indexMap[val] = len(self.content) - 1
        return True

    def remove(self, val: int) -> bool:

        if val in self.indexMap:

            removal_index = self.indexMap[val]

            if removal_index == len(self.content) - 1:
                self.content.pop()
                self.indexMap.pop(val)
                return True

            last_val = self.content[-1]
            to_remove = self.content[removal_index]

            self.content[-1] = to_remove
            self.content[removal_index] = last_val

            self.content.pop()
            self.indexMap.pop(to_remove)
            self.indexMap[last_val] = removal_index

            return True

        return False

    def getRandom(self) -> int:

        return random.choice(self.content)
