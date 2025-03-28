# problem link-->> https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows , cols = len(grid) , len(grid[0])
        q = [(n , i) for i , n in enumerate(queries)]
        q.sort()
        res = [0] * len(queries)
        count = 0

        min_heap = [(grid[0][0] , 0 , 0)]
        visit = set([(0,0)])

        for limit , index in q:
            while min_heap and min_heap[0][0] < limit:
                val , r, c = heappop(min_heap)
                count += 1
                directions = [(r,c+1) , (r , c-1) , (r+1 ,c) , (r-1 ,c)]
                for nr , nc in directions:
                    if (0 <= nr < rows and 0 <= nc < cols and (nr , nc) not in visit):
                        heappush(min_heap , (grid[nr][nc] , nr , nc))
                        visit.add((nr,nc))
            res[index] = count
        return res




        
