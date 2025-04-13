# problem link -- >> https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        summ = sum(stones)
        target = ceil(summ / 2)
        def dfs(i , total):
            if total >= target or i == len(stones):
                return abs(total - (summ - total))

            if ( i , total) in dp:
                return dp[(i , total)]

            dp[(i , total)] = min(dfs(i+1 , total + stones[i]) , dfs(i+1 , total))
            return dp[(i , total)]

        return dfs(0,0)

        
