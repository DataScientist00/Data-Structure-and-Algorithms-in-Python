# problem link-->> https://leetcode.com/problems/number-of-ways-to-split-array/description/


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        total = sum(nums)
        ans = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            if left_sum >= total - left_sum:
                ans += 1 
        return ans
