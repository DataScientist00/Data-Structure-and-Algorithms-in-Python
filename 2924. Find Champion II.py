# problem link-->> https://leetcode.com/problems/find-champion-ii/description/


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, visited)

            

        ans = []
        for i in range(n):
            visited = set()
            dfs(i , visited)
            if len(visited) == n:
                ans.append(i)
                
        return -1 if (len(ans) > 1 or len(ans) == 0) else ans[0]
        
