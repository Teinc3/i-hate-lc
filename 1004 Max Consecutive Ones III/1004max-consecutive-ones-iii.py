class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lptr = 0
        max_count = 0
        flip_count = 0
        for rptr, r_el in enumerate(nums):
            if r_el == 1:
                continue

            # must flip for r_el = 0 in order to continue sequence
            if flip_count < k:
                flip_count += 1
                continue

            # If cannot, record max, and retract lptr until it can be flipped
            max_count = max(max_count, rptr - lptr)
            while lptr <= rptr:
                if nums[lptr] == 0:
                    lptr += 1
                    break
                lptr += 1
        
        return max(max_count, len(nums) - lptr)
                