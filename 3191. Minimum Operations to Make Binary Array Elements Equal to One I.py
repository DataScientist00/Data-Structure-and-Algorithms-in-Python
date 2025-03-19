#problem link-->> https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums , i):
            nums[i] = 0 if nums[i] == 1 else 1
        
        res = 0
        for n in range(len(nums)-2):
            if nums[n] == 0:
                flip(nums , n)
                flip(nums , n+1)
                flip(nums , n+2)
                res += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return res
        
