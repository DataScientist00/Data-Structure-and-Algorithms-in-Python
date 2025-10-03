# problem link-->> https://leetcode.com/problems/trapping-rain-water-ii/description/


import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = [] #(height , x , y)
        visited = set()
        row = len(heightMap)
        cols = len(heightMap[0])

        # add boundary cells
        for c in [0, cols-1]:
            for r in range(row):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited.add((r, c))

        for r in [0, row-1]:
            for c in range(cols):
                if (r, c) not in visited:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited.add((r, c))

        ans = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while heap:
            box_h, r, c = heapq.heappop(heap)
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < row and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    ans += max(0, box_h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(heightMap[nr][nc], box_h), nr, nc))

        return ans
