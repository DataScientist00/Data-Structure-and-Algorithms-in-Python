# problem link-->> https://leetcode.com/problems/max-chunks-to-make-sorted/description/


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        maxx = -1
        for i , n in enumerate(arr):
            maxx = max(maxx , n)
            if maxx == i:
                res += 1
        return res
        
