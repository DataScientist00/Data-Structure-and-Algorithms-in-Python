# problem link-->> https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/



class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        memo = {}
        def dfs(i,j,target,turn,name):
            if 0 > i or i >= rows or 0 > j or j >= cols or grid[i][j] != target:
                return 0
            key = (i, j, target, turn, name) # we are storing copy becuase we are going to flip 'turn' variable in upcoming recursion call, so store it 
            if key in memo:
                return memo[key]
            target = 0 if target == 2 else 2
            temp = 0

            if turn:
                if name == 'top-right':
                    temp = max(temp , 1+dfs(i+1,j+1,target,True,'top-right'))
                elif name == 'top-left':
                    temp =  max(temp , 1+dfs(i-1,j+1,target,True,'top-left')) 
                elif name == 'bottom-left':
                    temp =  max(temp , 1+dfs(i-1,j-1,target,True,'bottom-left')) 
                elif name == 'bottom-right':
                    temp =  max(temp , 1+dfs(i+1,j-1,target,True,'bottom-right')) 

            else:
                if name == 'top-right':
                    temp =  max(temp , 1+dfs(i-1,j+1,target,False,'top-right')) 
                    temp = max(temp , 1+dfs(i+1,j+1,target,True,'top-right')) 
                elif name == 'top-left':
                    temp =  max(temp , 1+dfs(i-1,j-1,target,False,'top-left')) 
                    temp =  max(temp , 1+dfs(i-1,j+1,target,True,'top-left')) 
                elif name == 'bottom-left':
                    temp =  max(temp , 1+dfs(i+1,j-1,target,False,'bottom-left'))
                    temp =  max(temp , 1+dfs(i-1,j-1,target,True,'bottom-left'))
                elif name == 'bottom-right':
                    temp =  max(temp , 1+dfs(i+1,j+1,target,False,'bottom-right'))
                    temp =  max(temp , 1+dfs(i+1,j-1,target,True,'bottom-right'))
            memo[key] = temp
            return memo[key]


        for m in range(rows):
            for n in range(cols):
                if grid[m][n] == 1:
                    res = max(res ,1+ dfs(m-1,n+1,2,False,'top-right')) 
                    res =  max(res ,1+ dfs(m-1,n-1,2,False,'top-left'))
                    res =  max(res ,1+ dfs(m+1,n-1,2,False,'bottom-left'))
                    res =  max(res ,1+ dfs(m+1,n+1,2,False,'bottom-right'))
        return res
        
