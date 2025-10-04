# problem link-->> https://leetcode.com/problems/maximum-xor-for-each-query/description/


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        maxnum = 2 ** maximumBit - 1
        answer = []
        for n in reversed(nums):
            answer.append(xor ^ maxnum)
            xor ^= n

        return answer
        
