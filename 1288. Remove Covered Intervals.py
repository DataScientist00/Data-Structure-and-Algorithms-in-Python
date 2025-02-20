#problem link-->> http://leetcode.com/problems/remove-covered-intervals/description/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0] , -x[1]))
        res = [intervals[0]]
        for i , j in intervals[1:]:
            l , r = res[-1]
            if l <= i and r >= j:
                continue
            res.append([i,j])
        return len(res)

        
