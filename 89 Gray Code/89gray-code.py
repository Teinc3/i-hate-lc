class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        combinations = self.grayCode(n-1)
        new = []
        for bit in range(2):
            for x in (combinations if bit == 0 else reversed(combinations)):
                new.append(x | (bit << (n - 1)))
        return new