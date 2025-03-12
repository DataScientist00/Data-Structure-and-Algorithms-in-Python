# problem link-->> https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        res = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                res += 1
            elif nums[i] == 0:
                zeros += 1
            else:
                break
        return max(res , len(nums) - (res + zeros))

        

