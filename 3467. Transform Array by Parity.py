# problem link -- >> https://leetcode.com/problems/transform-array-by-parity/description/


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = 0
        even = 0
        for n in nums:
            if n % 2:
                odd += 1
            else:
                even += 1
        ans = []
        for i in range(len(nums)):
            if even:
                ans.append(0)
                even -= 1
                continue
            else:
                ans.append(1)
                odd -= 1
        return ans
        
