# problem link-->> https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0
        left, right = 1 , 2**(n-1)

        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                ans = 0 if ans else 1
        return ans
        
