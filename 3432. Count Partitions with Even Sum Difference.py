# problem link-->> https://leetcode.com/problems/count-partitions-with-even-sum-difference/description


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        total = sum(nums)
        result = 0
        for i in range(len(nums)-1):
            result += nums[i]
            if ((total - result) - result) % 2 == 0:
                ans += 1

        return ans
        
