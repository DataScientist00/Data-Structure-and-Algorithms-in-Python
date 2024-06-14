#problem link-->> https://leetcode.com/problems/sort-array-by-parity/description/


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer] % 2 == 0:
                nums[left_pointer] , nums[right_pointer] = nums[right_pointer] , nums[left_pointer]
                left_pointer += 1
        return nums

        
