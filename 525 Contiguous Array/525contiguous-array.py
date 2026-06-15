class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Make Prefix Sum Array
        # Then use dictionary to log indices
        # First and second step can be merged
        # Finally, sweep through each counter entry's min and max index 
        # Max O(n)

        cache = {
            0: -1
        }
        val = 0
        max_dist = 0
        for i, num in enumerate(nums):
            val += (1 if num == 1 else -1)
            
            if val in cache:
                max_dist = max(max_dist, i - cache[val])
            else:
                cache[val] = i
        
        return max_dist