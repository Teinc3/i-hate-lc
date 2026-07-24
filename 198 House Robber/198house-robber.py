class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.extend([0, 0]) # -1, -2 indexing
        for i in range(len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        
        return nums[-3]