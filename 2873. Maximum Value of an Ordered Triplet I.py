# problem link-->> http://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        maxx = 0
        for j in range(len(nums)):
            if nums[j] > maxx:
                maxx = nums[j]
                continue
            for k in range(j+1 , len(nums)):
                res = max(res, (maxx - nums[j] ) * nums[k])
        return res
        
