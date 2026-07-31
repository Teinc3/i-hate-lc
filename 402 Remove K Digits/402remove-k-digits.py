class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = num + "0"
        stack = []
        pops = 0
        for digit in num:
            while stack and stack[-1] > digit and pops < k:
                pops += 1
                stack.pop()
            stack.append(digit)
        stack.pop() # Remove the 0
        
        res = (''.join(stack)).lstrip("0")
        return res if res else "0"
