# problem link -- >> https://leetcode.com/problems/running-sum-of-1d-array/description/


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        summ = 0
        for n in nums:
            summ += n
            ans.append(summ)
        return ans
        
