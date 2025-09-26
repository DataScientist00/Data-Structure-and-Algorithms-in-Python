# problem link-->> https://leetcode.com/problems/valid-triangle-number/description


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    ans += (r-l)
                    l += 1                   
                else:
                    r -= 1
        return ans
        
