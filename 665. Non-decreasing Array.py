#problem link -- >> https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changes = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changes:
                return False
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changes = True
        return True
        
