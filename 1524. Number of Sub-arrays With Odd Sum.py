# problem link-->> https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = 0
        even = 0
        odd = 0
        ans = 0
        for n in arr:
            total += n
            if total % 2 == 1:
                ans = (ans + 1 + even)  % (10 ** 9 + 7)
                odd += 1
            else:
                ans = (ans + odd)  % (10 ** 9 + 7)
                even += 1
        return ans
        
