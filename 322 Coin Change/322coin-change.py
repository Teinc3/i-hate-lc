class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < min(coins):
            return -1
        
        kp = [float('inf')] * (amount + 1)
        kp[0] = 0
        for num in coins:
            for i in range(amount + 1):
                if i - num >= 0:
                    kp[i] = min(kp[i], 1 + kp[i - num])
        
        return kp[-1] if kp[-1] != float('inf') else -1