# problem link-->> https://leetcode.com/problems/magnetic-force-between-two-balls/description/


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def check(space):
            cnt = 1
            prev = position[0]
            for i in range(1 , len(position)):
                if position[i] >= space + prev:
                    cnt += 1
                    prev = position[i]
            if cnt >= m:
                return True
            return False

        l = 0
        r = max(position)
        ans = 0

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans
        
