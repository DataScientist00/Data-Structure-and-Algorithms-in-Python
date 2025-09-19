# problem link-->> https://leetcode.com/problems/maximum-width-ramp/description/



from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        max_nums = [0] * len(nums)
        prev_max = 0
        i = len(nums)-1
        for n in reversed(nums):
            max_nums[i] = max(n , prev_max)
            prev_max = max_nums[i]
            i -= 1
        
        l = 0
        res = float('-inf')
        for r in range(len(nums)):
            while nums[l] > max_nums[r]:
                l += 1
                continue
            res = max(res , r - l)
        return res
        

     
        
