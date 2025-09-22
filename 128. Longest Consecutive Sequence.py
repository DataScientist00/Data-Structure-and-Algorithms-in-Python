# problem link-->> https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        res = float('-inf')
        for n in nums:
            if n-1 not in nums:
                temp = 1
                t = n
                while t+1 in nums:
                    temp += 1
                    t += 1
                res = max(res , temp)
        return res
        
