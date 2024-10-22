#problem link-->> https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums)-1:
            maxjump = 0
            for i in range(l , r+1):
                maxjump = max(maxjump , i + nums[i])
            l = r + 1
            r = maxjump
            res += 1
        return res
        
