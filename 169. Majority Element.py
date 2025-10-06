
# problem link-->> https://leetcode.com/problems/majority-element/description/


# --------O(nlogn) + constant space----------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        for i in range(len(nums)-1):
            if (i - index) >= len(nums) // 2:
                return nums[i]
            if nums[i] != nums[i+1]:
                index = i
        return nums[0]



# -------O(n) + contant space ---------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        return res

        
