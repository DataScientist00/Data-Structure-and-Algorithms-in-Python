#problem link-->> https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for n in arr:
            prev = min(prev+1 , n)
        return prev
        
