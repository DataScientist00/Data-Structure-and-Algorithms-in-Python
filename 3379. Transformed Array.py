# problem link -- >> https://leetcode.com/problems/transformed-array/description/


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        M = len(nums)
        for i,n in enumerate(nums):
            if n > 0:
                p = (i+n) % M
                ans.append(nums[p])
            elif n == 0:
                ans.append(n)
            else:
                ans.append(nums[i-abs(n) % M])
        return ans
        
