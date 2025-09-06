# probleml ink-->> https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/description/



class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def solve(l , r):
            steps = 0
            L = 1 # R= 4*L - 1
            S = 1
            while L <= r:
                start = max(L , l)
                end = min(4*L - 1 , r)
                if start <= end:
                    steps += (end - start + 1) * S
                L *= 4
                S += 1
            return steps

        ans = 0
        for q in queries:
            q1 , q2 = q[0] , q[1]
            ans += (solve(q1, q2) + 1) // 2 
        return ans
            


        
