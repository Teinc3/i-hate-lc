class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        occurences = {}
        for num in nums:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1

        count = 0
        for num in occurences.keys():
            if k == 0:
                count += int(occurences[num] > 1)
            elif num + k in occurences:
                count += 1

        return count