# problem link-->> https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = 0
        for n in nums:
            if total > n:
                res = total + n
            total += n
        return res 
        
