#problem link-->> https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        summ = 0
        for n in nums:
            if n >= 10:
                summ += n
        return False if (sum(nums) - summ) == summ else True
        
