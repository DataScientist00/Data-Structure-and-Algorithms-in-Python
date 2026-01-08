# problem link_-->>> https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def ispossible(m):
            totalops = 0
            temp = 0
            for n in nums:
                temp = n // m
                if n % m == 0:
                    temp -=1 
                totalops += temp
            if totalops <= maxOperations:
                return True
            return False


        l = 1
        r = max(nums)
        result = 0
        while l<=r:
            mid = (l+r)//2
            if ispossible(mid):
                result = mid
                r = mid -1
            else:
                l = mid + 1
        return result

        
