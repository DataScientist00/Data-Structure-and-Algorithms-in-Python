# problem link-->> https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 **9 + 7
        ways = 1
        t=0
        minn = complexity[0]
        for i in range(1,len(complexity)):
            if complexity[i] <= minn:
                return 0
            minn = min(minn , complexity[i])
            t += 1
            ways = (ways * t) % MOD

        return ways
