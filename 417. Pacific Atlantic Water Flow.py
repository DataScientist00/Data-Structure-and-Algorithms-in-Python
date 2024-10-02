#problem link-->> https://leetcode.com/problems/pacific-atlantic-water-flow/description/


from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = deque()
        p_seen = set()
        
        atlantic = deque()
        a_seen = set()
        
        m, n = len(heights), len(heights[0])

        for j in range(n):
            pacific.append((0, j))
            p_seen.add((0, j))
            
        for i in range(1, m):
            pacific.append((i, 0))
            p_seen.add((i, 0))
            
        for i in range(m):
            atlantic.append((i, n - 1))
            a_seen.add((i, n - 1))
            
        for j in range(n - 1):
            atlantic.append((m - 1, j))
            a_seen.add((m - 1, j))

        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i,j))
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
            return coords
            
        a = get_coords(pacific, p_seen)
        b = get_coords(atlantic, a_seen)
        return list(a.intersection(b))
