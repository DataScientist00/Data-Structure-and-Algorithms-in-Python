#problem link --- >> https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 1:
                neg += 1
        if neg % 2 == 0:
            return 1
        else:
            return -1
