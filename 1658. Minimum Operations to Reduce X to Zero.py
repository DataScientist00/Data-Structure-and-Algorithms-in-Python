# problem link-->> https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum = 0
        max_window = -1
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while l <=r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1
            
            if cur_sum == target:
                max_window = max(max_window , r - l + 1)
        return -1 if max_window == -1 else len(nums) - max_window
        
