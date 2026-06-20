class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        k = (target + sum(nums))/2
        if abs(target) > total or k % 1 != 0:
            return 0

        k = int(k)
        kp = [0] * (k+1)
        kp[0] = 1
        for r_idx, num in enumerate(nums):
            for w_idx in range(k, -1, -1): # [1, k]
                kp[w_idx] = kp[w_idx]
                if w_idx >= num:
                    kp[w_idx] += kp[w_idx - num]
        
        return kp[-1]