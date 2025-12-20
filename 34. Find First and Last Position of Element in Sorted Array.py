# problem link-->> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_first(low,high):
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    high = mid-1
                else:
                    low = mid + 1
            return ans

        a = binary_first(0,len(nums)-1)


    
        def binary_last(low,high):
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans



        b = binary_last(0,len(nums)-1)
        return [a,b]


                


        
