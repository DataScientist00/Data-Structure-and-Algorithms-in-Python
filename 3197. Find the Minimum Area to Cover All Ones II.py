#problem link-->> https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/

#Hint to solve -->> 2 splits in grid gives us 3 rectangles


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        def area(a,b,m, n):
            maxm = maxn = float('-inf')
            minm = minn = float('inf')
            for i in range(a,b+1):
                for j in range(m,n+1):
                    if grid[i][j]:
                        minm = min(minm , i)
                        minn = min(minn , j)
                        maxm = max(maxm , i)
                        maxn = max(maxn , j)
            return ((maxm - minm)+1) *  ((maxn - minn)+1)

        res = temp = float('inf')
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                res = min(res ,area(0,i , 0,cols-1) + area(i + 1 ,rows-1, 0,j) + area(i+1 ,rows-1, j+1,cols-1),
                area(0,i , 0,j) + area(0,i ,j+1,cols-1) + area(i+1 ,rows-1, 0,cols-1) ,
                area(0,rows-1 , 0,j) + area(0 ,i, j+1,cols-1) + area(i+1 ,rows-1, j+1,cols-1) ,
                area(0,rows-1 , j+1,cols-1) + area(0,i,0,j) + area(i+1 ,rows-1, 0,j))

        for i in range(rows):
            for j in range(i ,rows):
                res = min(res , area(0,i,0,cols-1) + area(i+1 , j ,0,cols-1) + area(j+1 , rows-1 , 0 , cols-1))

        for i in range(cols):
            for j in range(i ,cols):
                res = min(res , area(0,rows-1,0,i) + area(0,rows-1,i+1,j) + area(0,rows-1,j+1,cols-1))

        return res

        




        
