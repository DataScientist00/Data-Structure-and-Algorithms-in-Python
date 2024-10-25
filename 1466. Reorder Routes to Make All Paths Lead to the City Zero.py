#problem link-->> https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        graph = { i:[] for i in range(n)}
        visit = set()
        result = 0
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(city):
            nonlocal edges , graph , visit , result
            for a in graph[city]:
                if a in visit:
                    continue
                if (a,city) not in edges:
                    result += 1
                visit.add(a)
                dfs(a)
        visit.add(0)
        dfs(0)
        return result
