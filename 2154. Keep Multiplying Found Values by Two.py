# problem link-->> https://leetcode.com/problems/keep-multiplying-found-values-by-two/description


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        check = set(nums)
        while original in check:
            original = 2 * original
        return original 
        
