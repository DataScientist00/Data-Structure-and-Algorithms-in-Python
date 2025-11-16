# problem link-->> https://leetcode.com/problems/map-of-highest-peak/description/



class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        q = deque()
        
        # Initialize water cells
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    q.append((i, j))
        
        # BFS directions
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                for dr , dc in dirs:
                    new_r , new_c = dr + r , dc + c
                    if 0 <= new_r < m and 0 <= new_c < n and height[new_r][new_c] == -1:
                        height[new_r][new_c] = height[r][c] + 1
                        q.append((new_r , new_c))

        return height
        
