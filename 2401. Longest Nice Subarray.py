#problem link-->> https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 0
        used_bits = 0
        left = 0

        for right in range(len(nums)):
            while used_bits & nums[right]:
                used_bits ^= nums[left]
                left += 1
            used_bits |= nums[right]
            max_length = max(max_length, right - left + 1)

        return max_length
