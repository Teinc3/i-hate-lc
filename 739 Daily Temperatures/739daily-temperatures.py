class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        # 73, 74, 75, [75, 71], [75, 71, 69], [75, 71, 72], [76], [76, 73]
        for i, temp in enumerate(temperatures):
            # Pop everything in stack and write to answer array
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                answer[idx] = i - idx
            stack.append((temp, i))
        
        return answer