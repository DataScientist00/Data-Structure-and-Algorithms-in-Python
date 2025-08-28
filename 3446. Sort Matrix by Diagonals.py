# problem link-->> https://leetcode.com/problems/sort-matrix-by-diagonals/description/

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        bottom_left = []
        top_right = []
        m = -1
        for i in range(len(grid)):
            m += 1
            for j in range(len(grid) - i):
                bottom_left.append(grid[m+j][j])
            bottom_left.sort(reverse = True)
            for j in range(len(grid) - i):
                grid[m+j][j] = bottom_left[j]
            bottom_left = []
        m = 0
        for i in range(1,len(grid[0])):
            m +=1
            for j in range(len(grid) - i):
                top_right.append(grid[j][m+j])
            top_right.sort()
            for j in range(len(grid) - i):
                grid[j][m+j] = top_right[j]
            top_right = []
        return grid


            
                

        
