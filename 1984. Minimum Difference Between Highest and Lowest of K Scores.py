#problem link-->> https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , r = 0 , k -1
        res = float('inf')
        while r < len(nums):
            res = min(res , nums[r] - nums[l])
            l += 1
            r += 1
        return res        
