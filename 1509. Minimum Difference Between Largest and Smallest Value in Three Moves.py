# problem link-->> https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float('inf')
        for l in range(4):
            r = len(nums) - 4 + l
            res = min(res , abs(nums[r] - nums[l]))
        return res
            

        
