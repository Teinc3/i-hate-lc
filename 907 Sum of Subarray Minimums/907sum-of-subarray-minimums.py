class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        acc = 0
        mod = 1_000_000_000 + 7
        stack = []
        arr.append(0)

        # Create the minimum monotonic stack
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                left_idx = stack[-1] if stack else -1
                acc = (acc + arr[idx] * (idx - left_idx) * (i - idx)) % mod
            stack.append(i)

        return acc
