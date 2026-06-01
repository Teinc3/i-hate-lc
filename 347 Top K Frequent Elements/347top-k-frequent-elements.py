import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 0
        
        buckets = [None] * (len(nums) + 1)
        for num, count in hashmap.items():
            if buckets[count]:
                buckets[count].append(num)
            else:
                buckets[count] = [num]
        
        top_k = []
        for num_s in reversed(buckets):
            if num_s is None:
                continue
            if len(top_k) + len(num_s) > k:
                return top_k + num_s[0:k-len(top_k)]
            else:
                top_k.extend(num_s)
        
        return top_k