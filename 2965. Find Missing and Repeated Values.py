#problem link-->> https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        counter = defaultdict(int)

        for i in range(N):
            for j in range(N):
                counter[grid[i][j]] += 1
        missing , double = 0,0
        for num in range(1,N*N + 1):
            if counter[num] == 0:
                missing = num
            if counter[num] == 2:
                double = num
        return [double , missing]

        
