# problem link-->> https://leetcode.com/problems/minimize-maximum-of-array/


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            res = max(res , math.ceil(total / (i+1)))
        return res
        
