#problem link-->> https://leetcode.com/problems/minimum-time-to-repair-cars/description/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def total_count(mid):
            tt = 0
            for r in ranks:
                tt += int(sqrt(mid / r))
            return tt
        low , high = 1 , ranks[0] * cars * cars
        res = -1
        while low <= high:
            mid = (low + high) // 2
            total = total_count(mid)
            if total >= cars:
                res = mid
                high = mid -1
            else:
                low = mid + 1
        return res



        
