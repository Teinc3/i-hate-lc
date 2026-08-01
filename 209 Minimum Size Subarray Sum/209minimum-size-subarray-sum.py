class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_len = len(nums)
        min_len = nums_len + 1
        curr_sum = 0
        lptr = 0
        rptr = 0
        while rptr < nums_len:
            curr_sum += nums[rptr]
            rptr += 1

            while curr_sum >= target:
                min_len = min(min_len, rptr - lptr)
                curr_sum -= nums[lptr]
                lptr += 1
        
        return 0 if min_len > nums_len else min_len