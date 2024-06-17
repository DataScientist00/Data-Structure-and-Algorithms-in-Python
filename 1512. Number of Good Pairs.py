#problem link-->> https://leetcode.com/problems/number-of-good-pairs/description/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        temp = {}
        for i in nums:
            if i in temp:
                result += temp[i]
                temp[i] += 1
            else:
                temp[i] = 1
        return result
        
