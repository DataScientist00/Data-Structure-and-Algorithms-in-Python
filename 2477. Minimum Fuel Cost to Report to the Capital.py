# problem link-->> https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for src , dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node , parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child , node)
                    res += int(ceil(p / seats))
                    passengers += p
            return passengers + 1

        res = 0
        dfs(0,-1)
        return res
