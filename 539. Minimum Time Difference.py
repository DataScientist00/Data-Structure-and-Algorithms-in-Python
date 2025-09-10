# problem link-->> https://leetcode.com/problems/minimum-time-difference/description/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        seen = set()
        for t in timePoints:
            h , m = map(int , t.split(':'))
            tt = h * 60 + m
            if tt in seen:
                return 0
            seen.add(tt)
        time = sorted(seen)
        res = 1441
        for i in range(1,len(time)):
            res = min(res , time[i] - time[i-1])

        res = min(res , 1440 - time[-1]+time[0])
        return res



        
