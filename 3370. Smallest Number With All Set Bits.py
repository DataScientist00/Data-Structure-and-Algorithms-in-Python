 # problem link-->> https://leetcode.com/problems/smallest-number-with-all-set-bits/description


class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(1,n+1):
            if 2 ** i -1 >= n:
                return 2 ** i -1
            
        
