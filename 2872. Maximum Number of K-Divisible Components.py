# problem link-->> https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = {i:[] for i in range(n)}
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0
        def dfs(node , parent):
            nonlocal components
            temp = values[node]
            for v in graph[node]:
                if v != parent:
                    temp += dfs(v,node)
                    temp %= k
            if temp % k == 0:
                components += 1
                return 0
            return temp

        dfs(0,-1)
        return components
