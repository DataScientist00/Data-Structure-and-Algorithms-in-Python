# problem link-->> https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        result = 0
        towers = list(map(lambda x: (x, 0), range(m)))

        for i in range(n):
            new_towers = []
            zeros = []

            for j, height in towers:
                if matrix[i][j]:
                    new_towers.append((j, height + 1))
                else:
                    zeros.append((j, 0))

            towers = new_towers + zeros

            for j in range(m):
                result = max(result, (j + 1) * towers[j][1])

        return result
        
