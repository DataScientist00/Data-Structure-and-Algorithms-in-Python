# problem link-->> https://leetcode.com/problems/count-the-number-of-fair-pairs/description/


import bisect
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, n in enumerate(nums):
            left = bisect.bisect_left(nums, lower - n, i + 1)
            right = bisect.bisect_right(nums, upper - n, i + 1)
            ans += (right - left)
        return ans
