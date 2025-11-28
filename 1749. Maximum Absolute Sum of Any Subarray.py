# problem link-->> https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pre = nums[0]
        arr_sum = nums[0]
        for i in range(1,len(nums)):
            arr_sum = max(nums[i] , nums[i] + arr_sum)
            max_pre = max(max_pre , arr_sum)
        
        min_pre = nums[0]
        arr_sum = nums[0]
        for i in range(1,len(nums)):
            arr_sum = min(nums[i] , nums[i] + arr_sum)
            min_pre = min(min_pre , arr_sum)
        return max(abs(max_pre) , abs(min_pre))

        
