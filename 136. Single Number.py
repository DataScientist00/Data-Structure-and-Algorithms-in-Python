#problem link--->> https://leetcode.com/problems/single-number/description/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res
        