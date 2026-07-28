import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            lo_v, mid_v, hi_v = nums[lo], nums[mid], nums[hi]
            
            if lo_v <= mid_v and mid_v > hi_v:
                # real_breakpoint is right of mid
                lo = mid + 1
            elif lo_v > mid_v and mid_v <= hi_v:
                # real breakpoint is left of mid
                hi = mid
            elif lo_v <= mid_v and mid_v <= hi_v:
                break # Monotonically increasing; objective is to find target now
            else:
                raise ValueError("Monotonic decreasing sequence?")

        lo, bp, hi = 0, lo, len(nums) - 1
        # query adjacents to breakpoint
        if bp != 0:
            # Check which section is target in
            lo_val, bp_val, hi_val = nums[lo], nums[bp], nums[hi]
            if bp_val <= target <= hi_val:
                lo = bp
            else:
                hi = bp - 1

        # Do one final binary search
        idx = bisect.bisect_left(nums, target, lo, hi+1)
        if idx > hi or nums[idx] != target:
            return -1
        return idx
