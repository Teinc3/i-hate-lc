from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # General case
        # gcd(n, k) = offset_count
        # n / offset_count = steps_count
        # Idea: Temp nums[0] -> nums[0] = nums[0-k]
        # And nums [0-k] = nums[(0-2k) % n]

        

        n = len(nums)
        if k == 0:
            return
        offset_count = gcd(n, k)

        # k passes, n/k steps
        for offset in range(offset_count):
            tmp = nums[offset]
            for i in range(int(n / offset_count)):
                nums[(-i * k + offset) % n] = nums[(-(i+1)*k + offset) % n]
            nums[(offset + k) % n] = tmp
        