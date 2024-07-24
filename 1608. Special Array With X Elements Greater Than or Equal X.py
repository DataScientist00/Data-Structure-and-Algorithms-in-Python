#problem link-->> https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(1,k+1):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count += 1
            if count == i:
                return i
        return -1


        
