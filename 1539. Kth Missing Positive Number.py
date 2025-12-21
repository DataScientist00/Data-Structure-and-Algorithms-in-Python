# problem link-->> https://leetcode.com/problems/kth-missing-positive-number/description/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        check = set(arr)
        for i in range(1,2001):
            if i in check:
                continue
            k -= 1
            if k == 0:
                ans = i
                break
        return ans
        
