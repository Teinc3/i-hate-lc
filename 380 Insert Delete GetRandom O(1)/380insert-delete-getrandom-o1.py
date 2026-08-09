import random

class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.indices)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices.pop(val)
        if len(self.arr) > 1 and self.arr[-1] != val:
            self.arr[idx] = self.arr.pop()
            self.indices[self.arr[idx]] = idx
        else:
            self.arr.pop()
        return True

    def getRandom(self) -> int:
        return self.arr[int(random.random() * len(self.arr))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()