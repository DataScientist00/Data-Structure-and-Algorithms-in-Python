# problem link-->> https://leetcode.com/problems/greatest-sum-divisible-by-three/description/


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        memo = {}
        def split(i , r):
            if (i,r) in memo:
                return memo[(i,r)]
            if i >= len(nums):
                if r % 3 == 0:
                    return 0
                else:
                    return float('-inf')
            
            take = nums[i] + split(i+1 ,(nums[i] + r) % 3)
            dont_take = split(i+1 , r)
            memo[(i,r)] = max(take , dont_take)
            return memo[(i,r)]

        return split(0,0)
        
        
