
# problem link-->> https://leetcode.com/problems/count-submatrices-with-all-ones/description/

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0

        def solve(arr):
            temp = 0
            temp2 = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    temp2 = 0
                else:
                    temp2 += 1
                temp += temp2
            return temp 

        for r in range(m):
            res = [1] * n
            for c in range(r,m):
                for t in range(n):
                    res[t] = res[t] & mat[c][t]
                ans += solve(res)
        return ans


        
