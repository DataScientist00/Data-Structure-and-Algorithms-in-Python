# problem link->> https://leetcode.com/problems/third-maximum-number/description/?cong=true


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = float('inf')
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                cnt += 1
            if cnt == 2:
                return nums[i]
        return nums[0]
            

        
