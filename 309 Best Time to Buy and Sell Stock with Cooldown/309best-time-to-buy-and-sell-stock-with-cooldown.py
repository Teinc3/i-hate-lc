class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = prices
        prices.append((float('-inf'), float('-inf'), 0))
        # The DP stores 3 possibilities/states
        # 1. state where we have stock on hand
        # 2. state where we just sold stock
        # 3. state where we last idled because we couldn't buy stock yet
        for i in range(len(prices) - 1):
            ytd_profit = prices[i - 1]
            ytd_profit_with, ytd_profit_sold, ytd_profit_idle = ytd_profit
            current_price = prices[i]

            # For possibility of having stock on hand
            # Must either BUY (3 -> 1) or KEEP (1 -> 1)
            tdy_profit_with = max(ytd_profit_with, ytd_profit_idle - current_price)

            # For possibility of selling stock, must transition as (1 -> 2)
            tdy_profit_sold = ytd_profit_with + current_price

            # For possibility of idling, transition from either:
            # Must either just sold stock (2 -> 3) or keep idling (3 -> 3)
            tdy_profit_idle = max(ytd_profit_sold, ytd_profit_idle)

            prices[i] = (tdy_profit_with, tdy_profit_sold, tdy_profit_idle)

        return max(prices[-2])

