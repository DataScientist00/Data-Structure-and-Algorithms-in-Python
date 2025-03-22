#problem link-->> http://leetcode.com/problems/count-the-number-of-complete-components/description/


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(v , comp):
            if v in visit:
                return
            visit.add(v)
            comp.append(v)
            for nei in adj[v]:
                dfs(nei , comp)
            return comp

        adj = defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visit = set()
        for v in range(n):
            if v in visit:
                continue
            component = dfs(v , [])
            if all(len(component) -1 == len(adj[v2]) for v2 in component):
                res += 1
        return res

        
