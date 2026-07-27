import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap, max_cap = max(weights), sum(weights)

        mid_cap = -1
        while min_cap <= max_cap:
            old_mid, mid_cap = mid_cap, (min_cap + max_cap) // 2
            if old_mid == mid_cap:
                return max_cap
            
            curr_cap = 0
            curr_day = 1
            for weight in weights:
                if curr_cap + weight > mid_cap:
                    curr_day += 1
                    curr_cap = weight
                    if curr_day > days:
                        break
                    continue
                curr_cap += weight
            
            if curr_day > days: # Takes too long. Increase capcity
                min_cap = mid_cap
            else: # Too much to spare. Decrease capacity.
                max_cap = mid_cap

        return max_cap
