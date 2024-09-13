#problem link-->> https://leetcode.com/problems/house-robber/

#---------------------Recursion-----------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i+2) + nums[i] , dp(i+1))   
            return memo[i]
        return dp(0)
#--------------------Bottom-up--------------------------

def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2] ,dp[i-1] )
        return dp[-1]

            


        
