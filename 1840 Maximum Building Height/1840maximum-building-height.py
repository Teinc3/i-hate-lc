class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort(key=lambda res: res[0], reverse=False)

        # Forward Pass
        for i in range(1, len(restrictions)):
            old_res, new_res = restrictions[i-1], restrictions[i]
            restrictions[i][1] = min(
                new_res[1], new_res[0] - old_res[0] + old_res[1]
            )
        
        last_res = restrictions[-1]
        if last_res[0] != n:
            restrictions.append([n, last_res[1] + n - last_res[0]])

        # Backward Pass
        for i in range(len(restrictions) - 2, -1, -1):
            new_res, old_res = restrictions[i], restrictions[i + 1]
            restrictions[i][1] = min(
                new_res[1], old_res[0] - new_res[0] + old_res[1]
            )
        
        # Final Pass
        max_height = 0
        for i in range(1, len(restrictions)):
            left_res, right_res = restrictions[i-1], restrictions[i]
            # height_gain = abs(distance diff) - abs(height diff)
            diff_distance = abs(left_res[0] - right_res[0])
            diff_height = abs(left_res[1] - right_res[1])
            height_gain = (diff_distance - diff_height) // 2
            max_height = max(
                max_height, max(left_res[1], right_res[1]) + height_gain
            )
        
        return max_height