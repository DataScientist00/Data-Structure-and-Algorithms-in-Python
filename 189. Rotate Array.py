#problem link-->> https://leetcode.com/problems/rotate-array/description/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def modify(a , b):
            while a < b:
                nums[a] , nums[b] = nums[b] , nums[a]
                a , b = a + 1 , b - 1

        k = k % len(nums)
        l , r = 0 , len(nums) - 1
        modify(l , r)
        l ,r = 0 , k -1
        modify(l , r)
        l , r = k , len(nums) - 1
        modify(l , r)
