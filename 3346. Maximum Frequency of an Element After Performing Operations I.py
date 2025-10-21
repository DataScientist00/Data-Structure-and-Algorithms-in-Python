# problem link-->> https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxnum = max(nums)+k
        freqcount = [0] * (maxnum+1)
        for n in nums:
            freqcount[n] += 1
        for n in range(1,len(freqcount)):
            freqcount[n] += freqcount[n-1]
        res = float('-inf')
        for n in range(1,maxnum+1):
            l = max(0,n-k)
            r = min(n+k , maxnum)
            maxoperations = freqcount[r] - (freqcount[l-1] if l > 0 else 0)
            targetnum = freqcount[n] - (freqcount[n-1] if n > 0 else 0)
            total = maxoperations - targetnum
            res = max(res , targetnum + min(total ,numOperations ))
        return res
