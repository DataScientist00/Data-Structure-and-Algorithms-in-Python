# problem link-->> https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        l = 0
        for r in range(1,len(nums)):
            if nums[l] >= nums[r]:
                temp = nums[r]
                nums[r] = nums[l] + 1
                res += nums[r] - temp
            l += 1
        return res
            
            


        
