# problem link-->> https://leetcode.com/problems/make-sum-divisible-by-p/description


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        rem = total % p
        ans = len(nums)
        prefix = 0
        seen = {0:-1}
        for i , n in enumerate(nums):
            prefix = (prefix + n) % p
            need = (prefix - rem) % p
            if need in seen:
                ans = min(ans , i - seen[need])
            seen[prefix] = i
        return ans if ans < len(nums) else -1
