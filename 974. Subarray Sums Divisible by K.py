# problem link-->> https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        reminder = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for n in nums:
            prefix_sum += n
            reminder = prefix_sum % k
            res += prefix[reminder]
            prefix[reminder] += 1

        return res
        
