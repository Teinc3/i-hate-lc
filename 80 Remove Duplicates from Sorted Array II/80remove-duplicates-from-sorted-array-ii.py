class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through nums
        curr_number = 0
        curr_count = 0
        none_count = 0
        i = 0
        
        for i in range(len(nums)):
            num = nums[i]
            if curr_number == num:
                curr_count += 1
            else:
                curr_number = num
                curr_count = 1
            
            if curr_count >= 3:
                none_count += 1
            
            nums[i] = None
            nums[i - none_count] = num

        for x in range(none_count):
            nums.pop()
        
        return len(nums)
