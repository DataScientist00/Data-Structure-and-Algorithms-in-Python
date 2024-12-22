#problem link--->> https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)
        r = len(nums) - 1
        for i , left in enumerate(nums):
            while (nums[r] + left ) > target and i <= r:
                r -= 1
            if i <=r:
                res += (2 ** (r-i))
                res %= mod
        return res
        
