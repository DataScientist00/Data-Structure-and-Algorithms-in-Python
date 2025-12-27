# problem link-->> https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check(m):
            temp = 0
            for i in range(len(dist)-1):
                temp += math.ceil(dist[i] / m)
            temp += dist[-1] / m 
            return temp

        low = 1
        high = 10000007
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid) <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        
