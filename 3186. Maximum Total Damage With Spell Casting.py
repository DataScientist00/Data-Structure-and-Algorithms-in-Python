#  problem link-->> https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/


# -------------------Recursion-------------

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        mp = Counter(power)
        for k ,v in mp.items():
            mp[k] = k*v
        unique = sorted(mp.keys())
        n = len(unique)

        @lru_cache
        def solve(i):
            if i >= n:
                return 0
            not_take = solve(i+1)
            take = mp[unique[i]]
            j = i+1
            j = bisect_right(unique, unique[i] + 2)
            take += solve(j)
            return max(take , not_take)

        return solve(0)

        
        
