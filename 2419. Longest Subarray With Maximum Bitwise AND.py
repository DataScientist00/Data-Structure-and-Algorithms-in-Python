# problem link-->> https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        res = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == maxx:
                temp += 1
            else:
                res = max(temp , res)
                temp = 0
        return max(res , temp)
            
            


        
