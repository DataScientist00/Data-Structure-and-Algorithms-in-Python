# problem link-->> https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count =0
        arr = nums[:]
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                count += 1
        if count == len(nums):
            return max(arr)

        return sum(set(nums))


        
