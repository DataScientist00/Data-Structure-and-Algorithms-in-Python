#problem link--->> http://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}  # Dictionary for memoization

        def dp(num):
            if num == 1:
                return 1  # Base case
            
            if num in memo:  # Return stored value if already computed
                return memo[num]
            
            max_product = 0
            for i in range(1, num):
                max_product = max(max_product, i * (num - i), i * dp(num - i))
            
            memo[num] = max_product  # Store result
            return max_product

        return dp(n)
        
