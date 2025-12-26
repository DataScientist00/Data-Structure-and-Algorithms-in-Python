# problem link-->> https://leetcode.com/problems/last-day-where-you-can-still-cross/description/


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def canwalk(day):
            nonlocal dirs
            matrix = [[0 for _ in range(col)] for _ in range(row)]
            
            for i in range(day + 1):
                x , y = cells[i]
                matrix[x-1][y-1] = 1
            
            queue = []
            for j in range(col):
                if  matrix[0][j] == 0:
                    queue += [(0,j)]

            while queue:
                for _  in range(len(queue)):
                    i , j  = queue.pop(0)
                    if matrix[i][j] == 1 or matrix[i][j] == 'X':
                        continue
                    if i == row -1:
                        return True
                    matrix[i][j] = 'X'

                    for di , dj in dirs:
                        di , dj = i + di , j + dj
                        if 0 <= di < row and 0 <= dj < col and matrix[di][dj] != 1 and matrix[di][dj] != 'X':
                            queue += [(di,dj)]
            return False



        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        n = len(cells)

        low , high = 1 , n - 1
        while low <= high:
            mid = (low + high) // 2
            if canwalk(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low
        
