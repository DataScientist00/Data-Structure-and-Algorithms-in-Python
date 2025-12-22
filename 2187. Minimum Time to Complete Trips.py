# problem link-->> https://leetcode.com/problems/minimum-time-to-complete-trips/description/


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:


        def total(t):
            temp = 0
            for i in range(len(time)):
                temp += (t // time[i])
            return temp


        low = 1
        high = min(time) * totalTrips
        ans = high
        while low <= high:
            mid = (low+high)//2
            tt = total(mid)
            if tt >= totalTrips:
                high = mid-1
                ans = min(mid,ans)
            else:
                low = mid+1
                
        return ans
        
