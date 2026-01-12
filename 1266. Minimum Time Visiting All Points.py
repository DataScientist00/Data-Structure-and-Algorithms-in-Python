# problem link-->> https://leetcode.com/problems/minimum-time-visiting-all-points/description/


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        # cost each one move = 1       
        time = 0
        for x in range(len(points)-1):
            start, end = points[x], points[x+1]
            time += max(abs(start[0]-end[0]), abs(start[1]-end[1]))

        return time
        
