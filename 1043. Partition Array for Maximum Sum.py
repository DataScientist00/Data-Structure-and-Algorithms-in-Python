# problem link-->> https://leetcode.com/problems/partition-array-for-maximum-sum/description/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]
            cur_max = 0
            res = 0
            for j in range( i , min(len(arr) , i + k)):
                cur_max = max(cur_max , arr[j])
                window_size = j - i + 1
                res = max(res , dp(j+1) + cur_max * window_size)
            cache[i] = res
            return res
        return dp(0)
        
