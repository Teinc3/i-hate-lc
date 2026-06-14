from collections import Counter
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        heap = []
        for num in ctr.keys():
            heap.append(num)
        heapq.heapify_max(heap)

        i = 0
        curr_el = None
        while i < k:
            curr_el = heapq.heappop_max(heap)
            i += ctr[curr_el]
        
        return curr_el