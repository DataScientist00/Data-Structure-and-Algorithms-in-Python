# problem link-->> https://leetcode.com/problems/maximum-total-importance-of-roads/description/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n
        for a , b in roads:
            edge_cnt[a] += 1
            edge_cnt[b] += 1

        res = 0
        degree = 1
        for n in sorted(edge_cnt):
            res = res + degree * n
            degree += 1
        return res
        
