# problem link-->> https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a , b ,c in roads:
            adj[a].append((b,c))
            adj[b].append((a,c))

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for node , dis in adj[i]:
                res = min(res , dis)
                dfs(node)
        
        res = float("inf")
        visit = set()
        dfs(1)
        return res
