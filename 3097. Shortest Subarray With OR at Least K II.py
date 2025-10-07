# problem link-->> https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def do_the_or():
            total = 0
            for i in range(32):
                if bitset[i] != 0:
                    total |= (1 << i)
            return total

        bitset = [0] * 32
        ans = float('inf')
        l = 0
        for r in range(len(nums)):
            for i in range(32):
                if (nums[r] >> i) & 1:
                    bitset[i] += 1
            or_sum = do_the_or()
            while l <= r and or_sum >= k:
                ans = min(ans , r-l+1)
                for i in range(32):
                    if (nums[l] >> i) & 1:
                        bitset[i] -= 1
                l += 1
                or_sum = do_the_or()
        return -1 if ans == float('inf') else ans
