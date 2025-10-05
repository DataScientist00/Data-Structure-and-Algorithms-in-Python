
# problem link-->> https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def possible(x):
            total = 0
            for q in quantities:
                total += math.ceil(q / x)
            return total <= n

        l = 1
        r = max(quantities)
        ans = r
        while l <= r:
            mid = (r+l) // 2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
        
