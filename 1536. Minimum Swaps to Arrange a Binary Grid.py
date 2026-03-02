# problem link -- >> https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        endzeros = [0]*n
        for i in range(n):
            j = n-1
            count = 0
            while j >= 0 and grid[i][j] == 0:
                count += 1
                j -= 1
            endzeros[i] = count
        steps = 0
        for i in range(n):
            need = n-i-1
            j = i
            while j < n and endzeros[j] < need:
                j += 1
            if j == n:
                return -1
            steps += (j-i)
            while j > i:
                endzeros[j] , endzeros[j-1] =  endzeros[j-1] , endzeros[j]
                j -= 1
        return steps
