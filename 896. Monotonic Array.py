#problem link-->> https://leetcode.com/problems/monotonic-array/description/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        Increasing , Decreasing = True , True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                Decreasing = False
            if nums[i] > nums[i+1]:
                Increasing = False
        return Increasing or Decreasing

        
