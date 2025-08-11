# problem link-->> https://leetcode.com/problems/range-product-queries-of-powers/description/

from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7 
        power = []
        
        # Extract powers of two from n
        for i in range(30):
            if n & (1 << i):
                power.append(2 ** i)
        ans = []
        for c1, c2 in queries:
            product = 1
            for i in range(c1, c2 + 1):
                product = (product * power[i]) % MOD
            ans.append(product)
        
        return ans
