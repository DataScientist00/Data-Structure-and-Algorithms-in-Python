# problem link-->> https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        temp1 = temp2 = 0
        res = float('-inf')
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
                temp2 = temp1
                temp1 = r
            if zeros > 1:
                l = temp2 + 1
                zeros -= 1
            res = max(res , r-l+1)
        return res-1

        
