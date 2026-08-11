import heapq

class MedianFinder:

    def __init__(self):
        self.lheap = []
        self.rheap = []

    def addNum(self, num: int) -> None:
        # l > r: add to l and move to r; add to r; add to r;
        # l = r: add to l; add to l; add to r and move to l;
        l_len = len(self.lheap)
        r_len = len(self.rheap)
        l_mid = self.lheap[0] if l_len else float('inf')
        r_mid = self.rheap[0] if r_len else float('-inf')

        if l_len > r_len:
            if num < l_mid:
                heapq.heappush_max(self.lheap, num)
                heapq.heappush(self.rheap, heapq.heappop_max(self.lheap))
            else:
                heapq.heappush(self.rheap, num)
        else:
            if num > r_mid:
                heapq.heappush(self.rheap, num)
                heapq.heappush_max(self.lheap, heapq.heappop(self.rheap))
            else:
                heapq.heappush_max(self.lheap, num)

    def findMedian(self) -> float:
        return self.lheap[0] if len(self.lheap) > len(self.rheap) else (self.lheap[0] + self.rheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()