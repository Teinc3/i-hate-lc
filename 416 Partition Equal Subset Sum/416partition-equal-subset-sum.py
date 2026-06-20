class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Sum A = Sum B -> Sum A = Sum AB / 2
        sum_total = sum(nums)
        if sum_total % 2 != 0:
            return False
        target = sum_total // 2

        kp = [False] * (target + 1)
        kp[0] = True

        for num in nums:
            for col_idx in range(target, num -1, -1):
                kp[col_idx] = kp[col_idx] or kp[col_idx - num]
        
        return kp[-1] 