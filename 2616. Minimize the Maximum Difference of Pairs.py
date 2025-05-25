# problem link-->> https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isvalid(limit):
            i , cnt = 0 ,0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= limit:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False
        if p ==0:
            return 0

        nums.sort()
        l , r = 0 , 10**9
        res = 10**9
        while l <=r:
            m = (l+r) //2
            if isvalid(m):
                res = m
                r = m-1
            else:
                l = m + 1
        return res
        
