# problem link-->> https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
                continue
            else:
                nums[j] = nums[i]
                j += 1
        t = -1
        for i in range(z):
            nums[t] = 0
            t -= 1
        return nums

        
            

        
