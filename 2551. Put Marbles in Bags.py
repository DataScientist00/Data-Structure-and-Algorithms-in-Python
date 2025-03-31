# problem link-->> https://leetcode.com/problems/put-marbles-in-bags/description/


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights) - 1
        weights = [weights[i] + weights[i + 1] for i in range(n)]
        weights.sort()
        res = 0
        for i in range(k - 1):
            res += weights[-1 - i] - weights[i]
        return res
        
