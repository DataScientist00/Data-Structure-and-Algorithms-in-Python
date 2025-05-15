# probleml ink-->> https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        Indegree = [0] * n

        for src , dst in edges:
            Indegree[dst] += 1 # the nodes with 0 Indegree will be the answers

        return [node for node in range(n) if Indegree[node] ==0]
        
