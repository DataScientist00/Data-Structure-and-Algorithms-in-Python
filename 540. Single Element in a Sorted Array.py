# problem link--> https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                if nums[m-1] == nums[m]:
                    l = m+1
                else:
                    r = m -1
            else:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m -1

        return nums[l]
        
