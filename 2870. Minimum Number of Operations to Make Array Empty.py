# problem link-->> https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for a , b in count.items():
            if b == 1:
                return -1
            res += math.ceil(b / 3)
        return res
        
