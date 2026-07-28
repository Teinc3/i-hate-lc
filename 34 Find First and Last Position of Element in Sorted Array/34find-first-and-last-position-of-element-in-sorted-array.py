class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        bounds = [-1, -1]

        while lo <= hi:
            mid = (lo + hi) // 2 # left-leaning
            mid_val = nums[mid]
            if mid_val == target:
                # Check if the left is the same
                if mid > 0 and nums[mid - 1] == target:
                    hi = mid - 1
                    continue
                bounds[0] = mid
                break
            elif mid_val < target:
                lo = mid + 1
            else:
                hi = mid - 1
                
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi + 1) // 2 # right-leaning
            mid_val = nums[mid]
            if mid_val == target:
                # Check if the left is the same
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    lo = mid + 1
                    continue
                bounds[1] = mid
                break
            elif mid_val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return bounds