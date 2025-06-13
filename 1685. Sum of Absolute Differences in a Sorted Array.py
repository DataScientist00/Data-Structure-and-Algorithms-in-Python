# problem link-->> https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        diff = sum(nums)

        for i, num in enumerate(nums):
            yield ((i << 1) - len(nums)) * num + diff
            diff -= num << 1
        
