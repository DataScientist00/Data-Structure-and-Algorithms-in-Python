# problem link-->> https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:            
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)
        ans = []
        for q1,q2 in queries:
            graph[q1].append(q2)
            q = deque()
            visit = set()
            q.append((0,0))
            visit.add(0)
            while q:
                node , distance = q.popleft()
                if node == n-1:
                    ans.append(distance)
                    break
                for t in graph[node]:
                    if t not in visit:
                        visit.add(t)
                        q.append((t,1+distance))          
        return ans
                

        
