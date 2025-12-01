# problem link-->> https://leetcode.com/problems/maximum-running-time-of-n-computers/description/


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def binary(mid):
            required = mid * n
            total = 0
            for t in batteries:
                total += min(t , mid)
            if total >= required:
                return True
            return False
        
        l = 0
        r = sum(batteries) // n
        ans = 0
        while l <= r:
            mid = (l+r) // 2
            if binary(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans


        
