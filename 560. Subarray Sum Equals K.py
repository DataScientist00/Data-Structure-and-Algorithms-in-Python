#problem link-->> https://leetcode.com/problems/subarray-sum-equals-k/description/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        summ = 0
        prefix = 0
        for n in nums:
            prefix += n
            if prefix - k in dic:
                summ += dic[prefix - k]
            if prefix in dic:
                dic[prefix] += 1
            else:
                dic[prefix] = 1
        return summ

        
