#problem link-->> https://leetcode.com/problems/combination-sum/description/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res , temp = [] , []
        def dfs(i):
            if sum(temp) == target:
                res.append(temp[:])
                return
            if sum(temp) > target or i >= len(candidates):
                return

            temp.append(candidates[i])
            dfs(i)
            temp.pop()
            dfs(i+1)

        dfs(0)             
        return res

                
        
