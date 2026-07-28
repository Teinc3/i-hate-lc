class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            cap = (lo + hi) // 2

            count = 1
            acc = 0
            for num in nums:
                if acc + num > cap:
                    count += 1
                    acc = 0
                acc += num
            
            if count <= k:
                # capacity is too much. 
                hi = cap
            else:
                # Not enough capacity
                lo = cap + 1

        return lo