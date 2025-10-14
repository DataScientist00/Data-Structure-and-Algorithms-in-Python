# problem link-->> https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/



class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l = 0
        check = set()
        for r in range(len(nums)):
            if r-1 >= 0 and nums[r-1] >= nums[r]:
                l = r
            if r-l+1 > k:
                l += 1
            if r-l+1 == k:
                check.add(r)
        for j in check:
            if j + k in check:
                return True
        return False
                
        
