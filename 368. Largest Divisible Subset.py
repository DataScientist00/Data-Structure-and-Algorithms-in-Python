# problem link-->> https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = [0] * n
        dp = [1] * n
        last = 0
        ans = []
        nums.sort()
        for i in range(n):
            h[i] = i
            for prev in range(0, i):
                if nums[i] % nums[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    h[i] = prev
            if dp[i] > dp[last]:
                last = i
        
        while h[last] != last:
            ans.append(nums[last])
            last = h[last]
        ans.append(nums[last])

        return ans[::-1]
        
