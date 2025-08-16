# problem link-->> https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for i ,j,k in edges:
            graph[i].append((j,k))
            graph[j].append((i,k))

        def dijkstra(src):
            heap = [(0,src)] # dist , node
            visit = set()
            while heap:
                dist , node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei , dist2 in graph[node]:
                    nei_dist = dist2 + dist
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap , (nei_dist , nei))

            return len(visit) - 1

        res , min_count = -1 , n
        for node in range(n):
            count = dijkstra(node)
            if count <= min_count:
                res , min_count = node , count
        return res



        
