#problem link-->> https://leetcode.com/problems/target-sum/description/


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i , total):
            if i == len(nums):
                return 1 if target == total else 0
            if (i,total) in memo:
                return memo[ (i ,total)]

            if i >= len(nums):
                return

            add = dp(i+1 , total + nums[i]) 
            sub = dp(i+1 , total - nums[i])
            memo[(i , total)] = add + sub
            return memo[(i , total)]
        
        return dp(0 , 0)

    
