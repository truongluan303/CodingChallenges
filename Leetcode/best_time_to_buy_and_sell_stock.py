class Solution:

    def max_profit(self, prices: list[int]) -> int:

        best_val = 0
        left_idx = 0

        for i in range(len(prices)):

            if prices[left_idx] > prices[i]:
                left_idx = i

            else:
                val = prices[i] - prices[left_idx]
                best_val = max(val, best_val)

        return best_val