#problem link-->> https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Step 1: Construct graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: Dijkstra's Algorithm Setup
        minHeap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        ways = [0] * n
        
        shortest_time[0] = 0
        ways[0] = 1
        
        while minHeap:
            cur_time, node = heapq.heappop(minHeap)
            
            if cur_time > shortest_time[node]:
                continue  # Ignore outdated paths
            
            for neighbor, time in graph[node]:
                new_time = cur_time + time

                # Found a shorter path to neighbor
                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(minHeap, (new_time, neighbor))

                # Found another shortest path to neighbor
                elif new_time == shortest_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
        
