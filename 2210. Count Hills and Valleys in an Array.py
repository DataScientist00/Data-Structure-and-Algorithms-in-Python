# problem link-->> https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        while j < len(nums) - 1:
            if (nums[i] < nums[j] and nums[j] > nums[j+1]) or (nums[i] > nums[j] and nums[j] < nums[j+1]):
                res += 1
                i = j
            j += 1
        return res
                
        
        
