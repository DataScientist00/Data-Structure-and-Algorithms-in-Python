# problem link-->>> https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = k * threshold
        l = 0
        summ = sum(arr[:k])
        ans = 0
        if summ >= total:
            ans += 1
        for r in range(k, len(arr)):
            summ = summ - arr[l] + arr[r]
            l += 1
            if summ >= total:
                ans += 1
        return ans
                

        
