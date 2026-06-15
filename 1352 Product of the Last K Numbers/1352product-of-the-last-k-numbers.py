class ProductOfNumbers:

    def __init__(self):
        self.pp = [1]
        self.zeros = [float('-inf')]

    def add(self, num: int) -> None:
        # Don't let a zero fuck up our calculations
        if num == 0:
            self.zeros.append(len(self.pp))
            self.pp.append(1)
        else:
            self.pp.append(self.pp[-1] * num)

    def getProduct(self, k: int) -> int:
        # If there is a zero within the range then return zero
        if len(self.pp) - self.zeros[-1] <= k:
            return 0
        return self.pp[-1] // self.pp[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)