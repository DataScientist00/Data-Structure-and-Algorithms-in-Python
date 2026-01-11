# problem link-->> https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        nums1 = set(nums)
        cnt = 1
        for i in range(len(nums)):
            if cnt not in nums1:
                ans.append(cnt)
            cnt += 1
        return ans
        
