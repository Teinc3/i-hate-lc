import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate, max_rate = 1, max(piles)
        mid = -1
        while min_rate <= max_rate:
            old_mid = mid
            mid = (min_rate + max_rate) // 2
            if old_mid == mid:
                return max_rate
            total_time = sum(math.ceil(pile / mid) for pile in piles)
            if total_time <= h:
                # eating too fast, slow down
                max_rate = mid
            else:
                # Not fast enough, increase speed (increase min_rate)
                min_rate = mid
        # Converges.
        return min_rate