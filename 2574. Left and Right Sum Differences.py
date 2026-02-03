# problem link -- >> https://leetcode.com/problems/left-and-right-sum-differences/description/


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ans
        
