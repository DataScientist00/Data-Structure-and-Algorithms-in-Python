#problem link-->> https://leetcode.com/problems/house-robber-ii/description/


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(i , nums):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+ dp(i+2 , nums) , dp(i+1 , nums))
            return memo[i]
        res1 = dp(0 , nums[:-1]) 
        memo.clear()  # Reset the memo for the second case
        res2 = dp(0 , nums[1:])
        return max(res1 , res2)
        
