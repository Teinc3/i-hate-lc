class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        cycle = len(nums)
        stack = []
        answers = [-1] * cycle

        # Do it twice
        for i in range(2 * cycle):
            while stack and nums[stack[-1] % cycle] < nums[i % cycle]:
                idx = stack.pop()
                if answers[idx % cycle] == -1:
                    answers[idx % cycle] = nums[i % cycle]
                else:
                    answers[idx % cycle] = min(answers[idx % cycle], nums[i % cycle])
            stack.append(i)

        return answers