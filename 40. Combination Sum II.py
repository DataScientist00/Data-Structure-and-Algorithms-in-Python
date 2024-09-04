#problem link-->> https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp , res = [] , []
        total = 0
        def dfs(i , total):
            if total == target:
                res.append(temp[:])
                return
            if total > target or i >= len(candidates):
                return
            total += candidates[i]
            temp.append(candidates[i])
            dfs(i+1 , total)
            total -= candidates[i]
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1 , total)
            
        dfs( 0 ,0)
        return res
            
