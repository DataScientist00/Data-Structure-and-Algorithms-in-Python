# problem link-->> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/?envType=daily-question&envId=2025-12-17



class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        n = len(prices)
        @cache
        def dfs(i, j, end_state):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if end_state else 0
            p = prices[i]
            if end_state == 0:
                return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
            if end_state == 1:
                return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            else: # elif end_state == 2
                return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)
        
        ans = dfs(n-1, k, 0)
        dfs.cache_clear()
        return ans
