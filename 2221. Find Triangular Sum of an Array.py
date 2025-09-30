# problem link-->> https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

# -------O(n) space ------

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        t = len(nums) - 1
        while t:
            newNums = []
            for i in range(len(nums)-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
            t -= 1
        return nums[0]


#------O(1) space -------------

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        t = len(nums) - 1
        temp = 0
        while t:
            for i in range(t):
                if i == 0:
                    nums[i] = ((nums[i] + nums[i+1]) % 10)
                else:
                    nums[i] = ((temp + nums[i+1]) % 10)
                temp = nums[i+1]
            t -= 1
        return nums[0]
