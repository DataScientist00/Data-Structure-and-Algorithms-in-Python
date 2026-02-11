# problem link -- >> https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for n in nums:
            if n < k:
                ans += 1
            else:
                break
        return ans
