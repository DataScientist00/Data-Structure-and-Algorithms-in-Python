# problem link-->> https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        if window == 0:
            return 0
        l = 0
        N = len(nums)
        zeros = 0
        res = float('inf')
        for r in range(len(nums)*2):
            if nums[r%N] == 0:
                zeros += 1
            if r - l + 1 == window:
                res = min(res , zeros) 
                if nums[l%N] == 0:
                    zeros -= 1
                l += 1
        return res

            

        
