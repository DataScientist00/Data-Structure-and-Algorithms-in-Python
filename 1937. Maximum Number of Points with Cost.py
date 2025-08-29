# problem link-->> https://leetcode.com/problems/maximum-number-of-points-with-cost/description/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        left = [0] * n
        right = [0] * n
        prev = points[0]
        for i in range(1,m):
            curr = points[i]
            for j in range(0,n):
                left[j] = max(prev[j] , left[j-1]-1 if j-1 >= 0 else -1 )
                right[n-j-1] = max(prev[n-j-1] , right[n-j]-1 if n-j < n else -1)
            for j in range(0,n):
                curr[j] += max(left[j], right[j])
            prev = curr
        return max(prev)
                
