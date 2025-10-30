# problem link-->>> https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1,len(target)):
            if target[i-1] < target[i]:
                ans += abs(target[i-1] - target[i])
        return ans
        
